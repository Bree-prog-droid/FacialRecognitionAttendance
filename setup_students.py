import sqlite3

# Connect to your database
conn = sqlite3.connect('attendance.db')
cursor = conn.cursor()

# Create students table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    student_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    registration_number TEXT NOT NULL,
    course TEXT NOT NULL,
    facial_data_path TEXT NOT NULL
)
''')

# Insert dummy students
students = [
    (1, 'Alice', '0001', 'Computer Science', 'dataset/1'),
    (2, 'Bob', '0002', 'Information Tech', 'dataset/2'),
    (3, 'Carol', '0003', 'Software Eng', 'dataset/3'),
    (4, 'Matthew', '0004', 'Software Eng', 'dataset/4'),
    (5, 'Victoria', '0005', 'Software Eng', 'dataset/5'),
    (6, 'Zulekha', '0006', 'Software Eng', 'dataset/6')
]




cursor.executemany("INSERT OR IGNORE INTO students VALUES (?, ?, ?, ?, ?)", students)

conn.commit()
conn.close()

print("Dummy students inserted successfully!")
