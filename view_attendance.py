import sqlite3

# Connect to the database
conn = sqlite3.connect("attendance.db")
cursor = conn.cursor()

# Fetch all attendance records
cursor.execute("SELECT * FROM attendance")
rows = cursor.fetchall()

# Print them neatly
print("Attendance Records:")
print("ID | Student_ID | Date       | Time     | Status")
print("-----------------------------------------------")
for row in rows:
    print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]}")

conn.close()
