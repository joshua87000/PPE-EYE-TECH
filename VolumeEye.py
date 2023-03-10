import cv2
import numpy as np
import dlib
import time
import math
import functools
import pyautogui

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

while True:
    _, frame = cap.read()

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)


    faces = detector(gray)

    
    
   
    for face in faces:
        
        x, y = face.left() , face.top()
        x1 ,y1 = face.right(), face.bottom()
     
        landmarks = predictor(gray,face)

        p1 = Point(landmarks,37)
        p2 = Point(landmarks,38)
        p3 = Point(landmarks,41)
        p4 = Point(landmarks,40)

        Pgauche = Point(landmarks,36)
        Pdroite = Point(landmarks,39)

        visageHaut = Point(landmarks,19)


        midHaut = Point.fromcoord(int((p1.px + p2.px)/2), int((p1.py + p2.py)/2),landmarks,0)
        midBas = Point.fromcoord(int((p3.px + p4.px)/2), int((p3.py + p4.py)/2),landmarks,0)


        ratio= distance_entre_points(Pgauche,Pdroite)/distance_entre_points(midHaut,midBas)
    

        if ratio > 6:
              cv2.putText(frame, "blink", (300, 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
              pyautogui.press('volumedown')

        if ratio < 3:
              cv2.putText(frame, "Big", (300, 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
              print("Up")
              pyautogui.press('volumeup')


   
   
    cv2.imshow("image",frame)
    key = cv2.waitKey(1)


    if key == 27:
        print("end")
        break


cap.release()