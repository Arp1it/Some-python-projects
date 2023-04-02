import face_recognition
import csv
import cv2
import os
from datetime import datetime
import numpy as np



now = datetime.now()
current_date = now.strftime("%Y-%m-%d")
current_time = now.strftime("%H:%M:%S")

with open(f"{current_date}.csv", "w", newline="") as obj:
    wobj = csv.writer(obj)

    wobj.writerow(["Roll no.", "Name", "Present", "Time"])

    cap = cv2.VideoCapture(0)

    os.chdir("F:/cwh pythprojects/faces")
    a = os.listdir()
    os.chdir("F:\cwh pythprojects")
    print(a)

    known_face_encod = []
    known_face_name = []

    for g, i in enumerate(a):
        a = i.split(".")[0]
        b = g+1
        c = face_recognition.load_image_file(f"faces/{i}")
        b = face_recognition.face_encodings(c)[0]

        known_face_name.append(a)
        known_face_encod.append(b)

    students = known_face_name.copy()
    student = sorted(students)
    print(student)

    while True:
        ret, frame = cap.read()

        # small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        # print(small_frame)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        face_locations = face_recognition.face_locations(gray)
        unknown_encoding = face_recognition.face_encodings(gray, face_locations)

        for face_encoding in unknown_encoding:
            results = face_recognition.compare_faces(known_face_encod, face_encoding)
            face_distance = face_recognition.face_distance(known_face_encod, face_encoding)
            best_match = np.argmin(face_distance)
            # print(best_match)
            # print(face_distance)
            # print(results)
            # print(results[best_match])
            if results[best_match]:
                name = known_face_name[best_match]
                # print(name, results[best_match])

            if name in known_face_name:
                font = cv2.FONT_HERSHEY_SIMPLEX
                org = (1, 25)
                fontscale = 1
                color = (0, 0, 255)
                thickness = 3

                cv2.putText(frame, name+" Present", org, font, fontscale, color, thickness)


                if name in students:
                    students.remove(name)
                    wobj.writerow([student.index(name)+1, name, "yes", current_time])

        cv2.imshow("Attendance", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break


    cap.release()
    cv2.destroyAllWindows()
