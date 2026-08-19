import cv2

camera = cv2.VideoCapture(0)

while True:
    success, frame = camera.read()

    if not success: 
        break

    frame = cv2.flip(frame, 1)

    # rectangle
    cv2.rectangle(frame, (200, 200), (420, 420), (0, 255, 0), 2)

    # circle
    cv2.circle(frame, (400, 400), 50, (255, 0, 0), 3)
    cv2.circle(frame, (200, 200), 50, (255, 0, 0), 3)

    # line
    cv2.line(frame, (50, 50), (500, 50), (0, 0, 255), 2)

    # text

    cv2.putText(
        frame,
        "My Drawing",
        (100, 80),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 0, 0),
        2
    )

    cv2.imshow("My Camera", frame)


    key = cv2.waitKey(1) & 0xFF

    if key == ord("s"):
        cv2.imwrite("camera_draw.jpg", frame)

    if key == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()