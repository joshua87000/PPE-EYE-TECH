import cv2
import numpy as np

cap = cv2.VideoCapture(r"C:\Users\Joshua\Downloads\OPENCV\videoEyeAF.avi")
#cap = cv2.VideoCapture(2)

while True:
    ret,frame = cap.read()
    cut = frame
   # cut = frame[50 : 300 , 50 : 350]

    gris = cv2.cvtColor(cut ,cv2.COLOR_BGR2GRAY)
    gris = cv2.GaussianBlur(gris , (7,7),0)
    _, threshold = cv2.threshold(gris ,30  , 255 , cv2.THRESH_BINARY_INV);
    _, threshold2 = cv2.threshold(gris , 140 , 230 , cv2.THRESH_BINARY);

    contours,hierachy =  cv2.findContours(threshold , cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours , key = lambda x: cv2.contourArea(x), reverse=True)
    for cnt in contours:
        cv2.drawContours(cut,[cnt], -1 , (0 , 0 , 255) , 2)
        break
    

    cv2.imshow("Filtre 1" , threshold)
    cv2.imshow("Filtre 2" , threshold2)
    cv2.imshow("frame" , cut)
    key = cv2.waitKey(30)
    if key == 27:
        break


cv2.destroyAllWindows()