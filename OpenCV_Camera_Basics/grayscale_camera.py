import cv2
import time

camera = cv2.VideoCapture(0)

while True:
    success, frame = camera.read()

    if not success: 
        break

    frame = cv2.flip(frame, 1)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow("Grayscale Camera", gray)

    key = cv2.waitKey(1) & 0xFF

    if key == ord("s"):
        print("Saving photo in 3 sec...")
        time.sleep(3)
        
        success, frame = camera.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        cv2.imwrite("grayscale_photo.jpg", gray)
        print("photo saved...")

    if key == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()
