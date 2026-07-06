import tkinter as tk
import os
from tkinter import messagebox

python_path = "C:/Users/ngugi/AppData/Local/Programs/Python/Python314/python.exe"
project_path = "C:/Users/ngugi/OneDrive/Desktop/FacialRecognitionAttendance"

def init_db():
    os.system(f'"{python_path}" "{project_path}/database.py"')
    messagebox.showinfo("Info", "Database script executed")

def capture_faces():
    os.system(f'"{python_path}" "{project_path}/face_recognition.py"')
    messagebox.showinfo("Info", "Face capture script executed")

def train_model():
    os.system(f'"{python_path}" "{project_path}/train_model.py"')
    messagebox.showinfo("Info", "Train model script executed")

def mark_attendance():
    os.system(f'"{python_path}" "{project_path}/main.py"')
    messagebox.showinfo("Info", "Attendance script executed")

root = tk.Tk()
root.title("Facial Recognition Attendance System")
root.geometry("400x300")

tk.Label(root, text="Welcome Lecturer", font=("Arial", 16)).pack(pady=10)

tk.Button(root, text="Initialize Database", width=25, command=init_db).pack(pady=5)
tk.Button(root, text="Capture Faces", width=25, command=capture_faces).pack(pady=5)
tk.Button(root, text="Train Model", width=25, command=train_model).pack(pady=5)
tk.Button(root, text="Mark Attendance", width=25, command=mark_attendance).pack(pady=5)

root.mainloop()
