import os
from datetime import datetime

import cv2
import face_recognition
import pandas as pd


# Folder containing the known/reference face images.
# Keep the actual dataset private and do not upload it to a public repository.
KNOWN_IMAGES_FOLDER = r"dataset"

ATTENDANCE_FILE = "attendance.csv"

# Load known faces and their names.
known_encodings = []
known_names = []

if os.path.isdir(KNOWN_IMAGES_FOLDER):
    for filename in os.listdir(KNOWN_IMAGES_FOLDER):
        if not filename.lower().endswith((".jpg", ".jpeg", ".png")):
            continue

        image_path = os.path.join(KNOWN_IMAGES_FOLDER, filename)
        image = face_recognition.load_image_file(image_path)
        encodings = face_recognition.face_encodings(image)

        if encodings:
            known_encodings.append(encodings[0])
            # Example: "Dheshna.jpg" -> "Dheshna"
            known_names.append(os.path.splitext(filename)[0])
            print(f"Encoded: {filename}")
        else:
            print(f"No face found in {filename}")
else:
    print(f"Dataset folder not found: {KNOWN_IMAGES_FOLDER}")

# Start webcam capture.
video_capture = cv2.VideoCapture(0)

# Track names already marked during this run.
attendance_list = set()

print("Starting face recognition. Press Q to quit.")

while True:
    ret, frame = video_capture.read()
    if not ret:
        print("Could not read from webcam.")
        break

    # Resize for faster processing.
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    # Detect faces and create encodings.
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(
        rgb_small_frame, face_locations
    )

    for face_encoding, face_location in zip(face_encodings, face_locations):
        name = "Unknown"

        if known_encodings:
            matches = face_recognition.compare_faces(
                known_encodings, face_encoding, tolerance=0.5
            )
            distances = face_recognition.face_distance(
                known_encodings, face_encoding
            )

            best_match_index = distances.argmin()

            if matches[best_match_index]:
                name = known_names[best_match_index]

                if name not in attendance_list:
                    attendance_list.add(name)

                    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    row = pd.DataFrame(
                        [[name, timestamp]],
                        columns=["Name", "Time"],
                    )

                    if os.path.exists(ATTENDANCE_FILE):
                        row.to_csv(
                            ATTENDANCE_FILE,
                            mode="a",
                            header=False,
                            index=False,
                        )
                    else:
                        row.to_csv(
                            ATTENDANCE_FILE,
                            mode="w",
                            header=True,
                            index=False,
                        )

                    print(f"Attendance marked: {name}")

        # Scale face coordinates back to the original frame size.
        top, right, bottom, left = face_location
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(
            frame,
            name,
            (left, max(top - 10, 20)),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2,
        )

    cv2.imshow("Face Recognition Attendance", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video_capture.release()
cv2.destroyAllWindows()

print("Session ended.")
print("Attendance:", sorted(attendance_list))
