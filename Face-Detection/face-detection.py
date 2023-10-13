from cvzone.FaceDetectionModule import FaceDetector
from cvzone.SerialModule import SerialObject
import cv2

arduino = SerialObject("COM5")
detector = FaceDetector(minDetectionCon=0.3)
cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()

    frame, bboxs = detector.findFaces(frame)
    arduino.sendData([len(bboxs)])

    cv2.imshow("Video", frame)
    cv2.waitKey(1)
