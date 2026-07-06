import streamlit as st
import sqlite3
import os

# Title
st.title("Facial Recognition Attendance System")

# Navigation menu
menu = st.sidebar.selectbox("Menu", ["Home", "Students", "Attendance Records"])

# Database connection
conn = sqlite3.connect("attendance.db")
cursor = conn.cursor()

if menu == "Home":
    st.subheader("Run Recognition")
    st.write("Click the button below to start face recognition.")
    if st.button("Start Recognition"):
        os.system("python main.py")

elif menu == "Students":
    st.subheader("Student List")
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    for row in rows:
        st.write(row)

elif menu == "Attendance Records":
    st.subheader("Attendance Records")
    cursor.execute("SELECT * FROM attendance")
    rows = cursor.fetchall()
    for row in rows:
        st.write(row)

conn.close()
