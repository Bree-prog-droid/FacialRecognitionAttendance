import sqlite3

conn = sqlite3.connect('attendance.db')
cursor = conn.cursor()

cursor.execute("SELECT student_id, name, registration_number, course FROM students")
records = cursor.fetchall()
conn.close()

for row in records:
    print(row)
