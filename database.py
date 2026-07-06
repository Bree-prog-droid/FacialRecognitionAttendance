import sqlite3

def init_db():
    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()

    # Students Table
    cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                        student_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        registration_number TEXT UNIQUE NOT NULL,
                        course TEXT NOT NULL,
                        facial_data_path TEXT NOT NULL)''')

    # Attendance Table
    cursor.execute('''CREATE TABLE IF NOT EXISTS attendance (
                        attendance_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        student_id INTEGER,
                        date TEXT,
                        time TEXT,
                        status TEXT,
                        FOREIGN KEY(student_id) REFERENCES students(student_id))''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    print("✅ Database initialized successfully!")
