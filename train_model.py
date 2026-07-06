import cv2
import numpy as np
import os

def train_model():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    path = "dataset/7"

    faces = []
    ids = []

    # Loop through all images in dataset/12345
    for image_name in os.listdir(path):
        image_path = os.path.join(path, image_name)
        img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

        if img is None:
            print(f"Skipping invalid file: {image_path}")
            continue

        # Resize for consistency
        face = cv2.resize(img, (200, 200))
        faces.append(face)
        ids.append(7)  # your student ID

    recognizer.train(faces, np.array(ids))
    recognizer.save("trainer.yml")
    print("✅ Training complete. Saved as trainer.yml")

train_model()
