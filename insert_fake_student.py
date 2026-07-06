import sqlite3

# Connect to your database file
conn = sqlite3.connect('attendance.db')
cursor = conn.cursor()

# Insert fake student records
cursor.execute("INSERT INTO students (student_id, name, registration_number, course, facial_data_path) VALUES (1, 'Alice', '0001', 'Computer Science', 'dataset/1')")
cursor.execute("INSERT INTO students (student_id, name, registration_number, course, facial_data_path) VALUES (2, 'Bob', '0002', 'Information Tech', 'dataset/2')")
cursor.execute("INSERT INTO students (student_id, name, registration_number, course, facial_data_path) VALUES (3, 'Carol', '0003', 'Software Eng', 'dataset/3')")

# Save changes and close connection
conn.commit()
conn.close()

print("Fake student records inserted successfully!")
