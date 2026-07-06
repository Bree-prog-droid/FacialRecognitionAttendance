import sqlite3

conn = sqlite3.connect("attendance.db")
cursor = conn.cursor()

# Show all tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print("Tables:", cursor.fetchall())

# Show all rows in students
cursor.execute("SELECT * FROM students;")
rows = cursor.fetchall()

print("\nStudents Table:")
for row in rows:
    print(row)

conn.close()
