import cv2
import os

def detect_and_capture_faces(student_name, reg_number, course):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    cam = cv2.VideoCapture(0)

    count = 0
    save_path = f"dataset/{reg_number}"
    os.makedirs(save_path, exist_ok=True)

    while True:
        ret, frame = cam.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            count += 1
            cv2.imwrite(f"{save_path}/{count}.jpg", gray[y:y+h, x:x+w])
            cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 2)

        cv2.imshow("Capturing Faces", frame)

        if cv2.waitKey(1)  & 0xFF == ord('q') or count >= 30:
            break

    cam.release()
    cv2.destroyAllWindows()
    print(f"✅ Captured {count} face samples for {student_name}")
import cv2
import os

def detect_and_capture_faces(student_name, reg_number, course):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    cam = cv2.VideoCapture(0)

    count = 0
    save_path = f"dataset/{reg_number}"
    os.makedirs(save_path, exist_ok=True)

    while True:
        ret, frame = cam.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            count += 1
            cv2.imwrite(f"{save_path}/{count}.jpg", gray[y:y+h, x:x+w])
            cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 2)

        cv2.imshow("Capturing Faces", frame)

        if cv2.waitKey(1) & 0xFF == ord('q') or count >= 30:
            break

    cam.release()
    cv2.destroyAllWindows()
    print(f"✅ Captured {count} face samples for {student_name}")
import cv2
import os

def detect_and_capture_faces(student_name, reg_number, course):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    cam = cv2.VideoCapture(0)

    count = 0
    save_path = f"dataset/{reg_number}"
    os.makedirs(save_path, exist_ok=True)

    while True:
        ret, frame = cam.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            count += 1
            cv2.imwrite(f"{save_path}/{count}.jpg", gray[y:y+h, x:x+w])
            cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 2)

        cv2.imshow("Capturing Faces", frame)

        if cv2.waitKey(1) & 0xFF == ord('q') or count >= 30:
            break

    cam.release()
    cv2.destroyAllWindows()
    print(f"✅ Captured {count} face samples for {student_name}")
if __name__ == "__main__":
    detect_and_capture_faces("Brenda", "12345", "Computer Science")