import sqlite3

# Connect to your database
conn = sqlite3.connect('attendance.db')
cursor = conn.cursor()

# Insert Brenda into the students table
cursor.execute("""
INSERT OR IGNORE INTO students 
(student_id, name, registration_number, course, facial_data_path) 
VALUES (7, 'Brenda', '0007', 'Computer Science', 'dataset/7')
""")

conn.commit()
conn.close()

print("Brenda inserted successfully!")
