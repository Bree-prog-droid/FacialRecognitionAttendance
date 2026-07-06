import sqlite3

conn = sqlite3.connect("attendance.db")
cursor = conn.cursor()

# Insert your student record
cursor.execute("""
INSERT INTO students (student_id, name, registration_number, course, facial_data_path)
VALUES (?, ?, ?, ?, ?)
""", (1, "Brenda", "12345", "Computer Science", "dataset/1"))

conn.commit()
conn.close()

print("Student added successfully!")

