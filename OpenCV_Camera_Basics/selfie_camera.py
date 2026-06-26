import cv2

camera = cv2.VideoCapture(0)

while True:
    success, frame = camera.read()

    if not success:
        break

    frame = cv2.flip(frame, 1)

    cv2.imshow("My Camera", frame)

    key = cv2.waitKey(1)

    if key == ord("s"): # press s to captured photo
        cv2.imwrite("captured_photo.jpg", frame)

    if key == ord("q"): # press q to exit
        break

camera.release()
cv2.destroyAllWindows()