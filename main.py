#Face Detection

import cv2

faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture("Dark-Phoenix-Cast.jpg") #For images.

#cap = cv2.VideoCapture(0) #For web cam just comment the previous line and uncomment this line.

while True:

    facedetection, img = cap.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(img, 1.1, 4)

    for (x, y, w, h) in faces:

        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 255, 255), 2)

    cv2.imshow("img", img)

    k = cv2.waitKey(0) & 0xFF #For web cam change the value 30 to 0.

    if k == 27:
        break

cap.release()
