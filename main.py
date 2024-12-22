from handDetection import HandDetection
import cv2

handDetection = HandDetection(min_detection_confidence=0.5, min_tracking_confidence=0.5)

webcam = cv2.VideoCapture(1)  # Open the webcam directly

while True:
    status, frame = webcam.read()
    frame = cv2.flip(frame, 1)
    handLandMarks = handDetection.findHandLandMarks(image=frame, draw=True)  # Corrected syntax

    cv2.imshow("Hand Landmark", frame)
    if cv2.waitKey(1) == ord('a'):
        break

cv2.destroyAllWindows()
webcam.release()