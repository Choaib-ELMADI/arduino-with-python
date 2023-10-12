from cvzone.SerialModule import SerialObject
import cv2

redOn = cv2.imread("red-on.png")
yellowOn = cv2.imread("yellow-on.png")
greenOn = cv2.imread("green-on.png")
allOff = cv2.imread("all-off.png")

arduino = SerialObject("COM6")

while True:
    arduino.sendData([1, 0, 0])
    cv2.imshow("LEDs", redOn)
    cv2.waitKey(500)

    arduino.sendData([0, 1, 0])
    cv2.imshow("LEDs", yellowOn)
    cv2.waitKey(500)

    arduino.sendData([0, 0, 1])
    cv2.imshow("LEDs", greenOn)
    cv2.waitKey(1000)

    arduino.sendData([0, 0, 0])
    cv2.imshow("LEDs", allOff)
    cv2.waitKey(500)
