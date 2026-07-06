import cv2
import sqlite3
import datetime

# Load the trained model
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainer.yml")

# Load the face detector
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Connect to the database
conn = sqlite3.connect("attendance.db")
cursor = conn.cursor()

# Helper function to get student name from database
def get_name(student_id):
    cursor.execute("SELECT name FROM students WHERE student_id=?", (student_id,))
    result = cursor.fetchone()
    if result:
        return result[0]   # returns the name, e.g. "Brenda"
    else:
        return "Unknown"

# Start webcam
cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()
    if not ret:
        print("Failed to grab frame")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        roi_gray = gray[y:y+h, x:x+w]

        # Predict ID and confidence
        id_, confidence = recognizer.predict(roi_gray)

        # Confidence check (lower = better match)
        if confidence < 120:   # adjust threshold if needed
            name = get_name(id_)
        else:
            name = "Unknown"

        # Draw rectangle and text
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.putText(frame, f"{name} - Present", (x, y-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,0), 2)

        # Insert attendance record if recognized
        if name != "Unknown":
            now = datetime.datetime.now()
            date_str = now.date().isoformat()
            time_str = now.time().strftime("%H:%M:%S")

            cursor.execute(
                "INSERT INTO attendance (student_id, date, status) VALUES (?, ?, ?)",
                (id_, date_str, "Present")
            )
            conn.commit()

    cv2.imshow("Attendance System", frame)

    # Press q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cam.release()
cv2.destroyAllWindows()
conn.close()
