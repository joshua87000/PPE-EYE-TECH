import cv2
import numpy as np
import dlib
import time
import math
import functools
import pyautogui
import subprocess

class Point:
    def __init__(self, land, nmb):
        self.px = land.part(nmb).x
        self.py = land.part(nmb).y

    def fromcoord(cls,px,py,land,nmb):
        p = cls(land,nmb)
        p.px = px
        p.py = py
        return p
    fromcoord = classmethod(fromcoord)

def onMouseClick(event, x, y, flags, param,add):
    if event == cv2.EVENT_LBUTTONUP:
        print(add)

def distance_entre_points(point1, point2):
    distance = math.sqrt((point2.px - point1.px)**2 + (point2.py - point1.py)**2)
    return distance

def draw_line_between_points(point1, point2, frame, color=(0, 255, 0), thickness=2):
    cv2.line(frame, (point1.px, point1.py), (point2.px, point2.py), color, thickness)


def draw_point(point):
    cv2.circle(frame, (point.px, point.py), 5, (0, 0, 255), -1)


def draw_polyline(point_list, frame):
   points = np.array([[p.px, p.py] for p in point_list], dtype=np.int32)
   cv2.polylines(frame, points, isClosed=False, color=(0, 0, 255), thickness=2)



detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(r"C:\Users\Joshua\Desktop\PPE EYE TECH\shape_predictor_68_face_landmarks.dat")

cap = cv2.VideoCapture(1)

fps = 0
start_time = time.time()

temps1L = time.time()
doubleCloseL = 0

temps1R = time.time()
doubleCloseR = 0

while True:
    _, frame = cap.read()

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)


    faces = detector(gray)

    
    
   
    for face in faces:
        
        x, y = face.left() , face.top()
        x1 ,y1 = face.right(), face.bottom()
     
        landmarks = predictor(gray,face)

        p1L = Point(landmarks,37)
        p2L = Point(landmarks,38)
        p3L = Point(landmarks,41)
        p4L = Point(landmarks,40)

        p1R = Point(landmarks,43)
        p2R = Point(landmarks,44)
        p3R = Point(landmarks,47)
        p4R = Point(landmarks,46)



        for i in range(68):
            P = Point(landmarks,i)
            cv2.circle(frame,(P.px,P.py),1,(0, 0, 255),1)

        PgaucheL = Point(landmarks,36)
        PdroiteL = Point(landmarks,39)

        PgaucheR = Point(landmarks,42)
        PdroiteR = Point(landmarks,45)

        visageHaut = Point(landmarks,19)


        midHautL = Point.fromcoord(int((p1L.px + p2L.px)/2), int((p1L.py + p2L.py)/2),landmarks,0)
        midBasL = Point.fromcoord(int((p3L.px + p4L.px)/2), int((p3L.py + p4L.py)/2),landmarks,0)

        midHautR = Point.fromcoord(int((p1R.px + p2R.px)/2), int((p1R.py + p2R.py)/2),landmarks,0)
        midBasR = Point.fromcoord(int((p3R.px + p4R.px)/2), int((p3R.py + p4R.py)/2),landmarks,0)


        ratioL = distance_entre_points(PgaucheL,PdroiteL)/distance_entre_points(midHautL,midBasL)
        ratioR = distance_entre_points(PgaucheR,PdroiteR)/distance_entre_points(midHautR,midBasR)


    

        if ratioL > 6:
              cv2.putText(frame, "blink", (300, 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
              if(doubleCloseL == 0):
                  time1L = time.time()
                  doubleCloseL = 1

              elif(doubleCloseL == 2):
                  difference = time.time()-time1L
                  print("double")
                  doubleCloseL = 3
                  #subprocess.Popen('"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"')
                  pyautogui.press('volumedown')
                 
        else:
            if(doubleCloseL == 1):
                doubleCloseL = 2
            elif(doubleCloseL == 3):
                doubleCloseL = 0
                
        if(doubleCloseL == 2 and (time.time() - time1L) > 0.5):
            doubleCloseL = 0
            print("simple L - ")
            print(time.time() - time1L)



        if ratioR > 6:
                cv2.putText(frame, "blink", (300, 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                if(doubleCloseR == 0):
                    time1R = time.time()
                    doubleCloseR = 1

                elif(doubleCloseR == 2):
                    difference = time.time()-time1R
                    print("double")
                    doubleCloseR = 3
                    #subprocess.Popen('"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"')
                    pyautogui.press('volumeup')
                    
        else:
            if(doubleCloseR == 1):
                    doubleCloseR = 2
            elif(doubleCloseR == 3):
                    doubleCloseR = 0
                    
            if(doubleCloseR == 2 and (time.time() - time1R) > 0.5):
                doubleCloseR = 0
                print("simple R - ")
                print(time.time() - time1R)

            
            
                


        if ratioL < 3:
              cv2.putText(frame, "Big", (300, 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
             
              


   
   
    cv2.imshow("image",frame)
    key = cv2.waitKey(1)


    if key == 27:
        print("end")
        break


cap.release()