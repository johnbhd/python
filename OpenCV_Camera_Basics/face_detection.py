import cv2

camera = cv2.VideoCapture(0)

face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

while True:
    success, frame = camera.read()

    if not success:
        break

    frame = cv2.flip(frame, 1)

    gray_for_detection = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_detector.detectMultiScale(
        gray_for_detection,
        scaleFactor=1.1,
        minNeighbors=5
    )

    for x, y, width, height in faces:
        cv2.putText(
            frame,
            "This is person is pogi",
            (x - 80, y -10),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255, 255, 255),
            2
        )
        cv2.rectangle(
            frame,
            (x, y),
            (x + width, y + height),
            (0, 255, 0), 
            2
        )

    cv2.imshow("Face Detection", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord("s"):
        cv2.imwrite("person.jpg", frame)

    if key == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()