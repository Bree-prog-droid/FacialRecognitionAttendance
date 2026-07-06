import tkinter as tk
from tkinter import messagebox
import sqlite3

import subprocess

def start_recognition():
    # This will run your main.py script
    subprocess.Popen(["python", "main.py"])

    

def view_students():
    conn = sqlite3.connect('attendance.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name, registration_number, course FROM students")
    records = cursor.fetchall()
    conn.close()

    # Format records nicely
    output = "\n".join([f"{name} ({reg}) - {course}" for name, reg, course in records])
    messagebox.showinfo("Student Records", output if output else "No students found.")

def view_attendance():
    conn = sqlite3.connect('attendance.db')
    cursor = conn.cursor()
    cursor.execute("SELECT student_id, date, status FROM attendance")
    records = cursor.fetchall()
    conn.close()

    # Format records nicely
    output = "\n".join([f"ID {sid} - {date} : {status}" for sid, date, status in records])
    messagebox.showinfo("Attendance Records", output if output else "No attendance found.")

# Create the main window
root = tk.Tk()
root.title("Attendance Dashboard")
root.geometry("400x300")

# Add buttons
btn_start = tk.Button(root, text="Start Face Recognition", command=start_recognition, width=25)
btn_start.pack(pady=10)

btn_view_students = tk.Button(root, text="View Students", command=view_students, width=25)
btn_view_students.pack(pady=10)

btn_view_attendance = tk.Button(root, text="View Attendance", command=view_attendance, width=25)
btn_view_attendance.pack(pady=10)

# Run the dashboard
root.mainloop()
