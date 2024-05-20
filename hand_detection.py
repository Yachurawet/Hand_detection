import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
detector = HandDetector()

while True:
    ret, frame = cap.read()
    if ret:
        hand, img_out = detector.findHands(frame)
        cv2.imshow('img_out', img_out)
    if cv2.waitKey(1) == ord('w'):
        break
cap.release()
cv2.destroyAllWindows()  
