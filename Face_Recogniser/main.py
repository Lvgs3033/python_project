import cv2
from test import Face_Recognition

sfr = Face_Recognition()
sfr.load_encoding_images("image/")

cap = cv2.VideoCapture(0) 

while True:
    ret, frame = cap.read()

    face_locations, face_names, accuracy_scores = sfr.detect_known_faces(frame)
    for face_loc, name, accuracy in zip(face_locations, face_names, accuracy_scores):
        y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

        label = f"{name} {accuracy:.2f}%"
        cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 150, 0), 2)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 150, 0), 4)

        print(f"Name: {name}, Accuracy: {accuracy:.2f}%")

    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 27:  
        break

cap.release()
cv2.destroyAllWindows()