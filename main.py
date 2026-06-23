import sqlite3
import database
from student import Student


def add_student():

    roll_no = int(input("Enter Roll No: "))
    name = input("Enter Name: ")

    marks = []

    for i in range(3):
        mark = float(input(f"Enter marks of subject {i+1}: "))
        marks.append(mark)

    student = Student(roll_no, name, marks)

    conn = sqlite3.connect("data/students.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO students VALUES(?,?,?,?,?,?)",
        (
            student.roll_no,
            student.name,
            str(student.marks),
            student.total,
            student.percentage,
            student.calculate_grade()
        )
    )

    conn.commit()
    conn.close()

    print("Student Added Successfully")


def view_students():

    conn = sqlite3.connect("data/students.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")

    records = cursor.fetchall()

    if len(records) == 0:
        print("No Records Found")

    else:

        for row in records:

            print("\nRoll No :", row[0])
            print("Name :", row[1])
            print("Marks :", row[2])
            print("Total :", row[3])
            print("Percentage :", round(row[4], 2))
            print("Grade :", row[5])

    conn.close()


def search_student():

    roll_no = int(input("Enter Roll Number : "))

    conn = sqlite3.connect("data/students.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM students WHERE roll_no=?",
        (roll_no,)
    )

    row = cursor.fetchone()

    if row:

        print("\nStudent Found")
        print("Roll No :", row[0])
        print("Name :", row[1])
        print("Marks :", row[2])
        print("Total :", row[3])
        print("Percentage :", round(row[4],2))
        print("Grade :", row[5])

    else:

        print("Student Not Found")

    conn.close()


def delete_student():

    roll_no = int(input("Enter Roll Number : "))

    conn = sqlite3.connect("data/students.db")
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM students WHERE roll_no=?",
        (roll_no,)
    )

    conn.commit()
    conn.close()

    print("Record Deleted Successfully")


while True:

    print("\n===== STUDENT RESULT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter Choice : ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        break

    else:
        print("Invalid Choice")