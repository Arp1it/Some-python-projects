import face_recognition
import numpy as np
import cv2
import csv
from datetime import datetime
import os


video_capture = cv2.VideoCapture(0)

a = os.chdir("faces/")
c = os.listdir()
os.chdir("F:\cwh pythprojects")

known_face_encodings = []
known_face_names = []
# # Load Known Faces
for a, i in enumerate(c):
    print(i)
    b = a+1
    a = face_recognition.load_image_file(f"faces/{i}")
    b = face_recognition.face_encodings(a)[0]

    # rohan_image = face_recognition.load_image_file("faces/rohan.jpg")
    # rohan_encoding = face_recognition.face_encodings(rohan_image)[0]

    known_face_encodings.append(b)
    known_face_names.append(i.split(".")[0])
print(known_face_names)
print(known_face_encodings)

# list of expected students
students = known_face_names.copy()

face_locations = []
face_encodings = []

# Get the current date and Time
now = datetime.now()
current_date = now.strftime("%Y-%m-%d")

f = open(f"{current_date}.csv", "w+", newline="")
lnwriter = csv.writer(f)


while True:
    _, frame = video_capture.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    # Recognize faces
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        face_distance = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distance)

        if(matches[best_match_index]):
            name = known_face_names[best_match_index]

        # Add the text if a person is present
        if name in known_face_names:
            font = cv2.FONT_HERSHEY_SIMPLEX
            bootomLeftCornerofText = (5, 30)
            fontScale = 1.0
            fontColor = (0, 0, 0)
            thickness = 3
            lineType = 2

            cv2.putText(frame, name + " Present", bootomLeftCornerofText, font, fontScale, fontColor, thickness, lineType)

            if name in students:
                students.remove(name)
                current_time = now.strftime("%H-%M-%S")
                lnwriter.writerow([name, current_time])

    cv2.imshow("Attendance", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


video_capture.release()
cv2.destroyAllWindows()
f.close()   