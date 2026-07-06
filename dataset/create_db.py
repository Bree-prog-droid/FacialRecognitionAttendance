import sqlite3

# Create a brand new database
conn = sqlite3.connect('attendance.db')
cursor = conn.cursor()

# Create students table
cursor.execute('''
CREATE TABLE students (
    student_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    registration_number TEXT NOT NULL,
    course TEXT NOT NULL,
    facial_data_path TEXT NOT NULL
)
''')

# Create attendance table
cursor.execute('''
CREATE TABLE attendance (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    date TEXT,
    status TEXT,
    FOREIGN KEY(student_id) REFERENCES students(student_id)
)
''')

conn.commit()
conn.close()

print("Fresh database created successfully!")
