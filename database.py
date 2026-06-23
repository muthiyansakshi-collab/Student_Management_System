import sqlite3

conn = sqlite3.connect("data/students.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
roll_no INTEGER PRIMARY KEY,
name TEXT,
marks TEXT,
total REAL,
percentage REAL,
grade TEXT
)
""")

conn.commit()
conn.close()