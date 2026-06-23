import sqlite3
import pandas as pd


def generate_report():

    conn = sqlite3.connect("data/students.db")

    df = pd.read_sql_query(
        "SELECT * FROM students",
        conn
    )

    df.to_csv(
        "student_report.csv",
        index=False
    )

    conn.close()

    print("Report Generated Successfully!")
