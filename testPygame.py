import cv2
import numpy as np
import dlib
import time
import math

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

       # draw_point(visageHaut)

        point_list = [Pgauche,p1,p2,Pdroite,p4,p3,Pgauche]
        points = np.array([[p.px, p.py] for p in point_list], dtype=np.int32)
      
        height , width, _ = frame.shape
        mask = np.zeros(( height , width), np.uint8)
        cv2.polylines(mask, [points],True,255,2)
        cv2.fillPoly(mask ,[points],255)
        LeftEyeMask = cv2.bitwise_and(gray,gray, mask = mask)

       # coloreye = LeftEyeMask[np.min(points[:,1]) : np.max(points[:,1]),np.min(points[:,0]) : np.max(points[:,0])]
        grayEye = LeftEyeMask[np.min(points[:,1]) : np.max(points[:,1]),np.min(points[:,0]) : np.max(points[:,0])]
      
       
        _, treshold_eye = cv2.threshold(grayEye,47,255,cv2.THRESH_BINARY)
       

       

        treshold_eye = cv2.resize(treshold_eye, None , fx = 10, fy = 10)

        height, width = treshold_eye.shape
        cv2.line(treshold_eye, (0,int(height/2)), (width,int(height/2)),(0,255,0), 2)
        cv2.line(treshold_eye, (int(width/2),0), (int(width/2),height),(0,255,0), 2)

        print(height)
        print(int(height/2))
        print("---")

        region1 = treshold_eye[0 : int(height/2) ,0 : int(width/2)]
        region4 = treshold_eye[int(height/2) : height ,int(width/2) :width]
        region2 = treshold_eye[0 : int(height/2) ,int(width/2) :width]
        region3 = treshold_eye[int(height/2) : height ,0 : int(width/2)]
        
        
       


        
        


        #coloreye = cv2.resize(coloreye, None , fx = 10, fy = 10)

        


      
      #  cv2.imshow("Eye2",coloreye)

        cv2.polylines(frame, [points], isClosed=False, color=(0, 0, 255), thickness=2)


        midHaut = Point.fromcoord(int((p1.px + p2.px)/2), int((p1.py + p2.py)/2),landmarks,0)
        midBas = Point.fromcoord(int((p3.px + p4.px)/2), int((p3.py + p4.py)/2),landmarks,0)

        #draw_line_between_points(midHaut,midBas,frame)
        #draw_line_between_points(Pgauche,Pdroite,frame)

        ratio= distance_entre_points(Pgauche,Pdroite)/distance_entre_points(midHaut,midBas)
    

        if ratio > 6:
              cv2.putText(frame, "blink", (300, 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        if ratio < 3:
              cv2.putText(frame, "Big", (300, 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)


        #cv2.line(frame, (p3.px,p3.py), (p4.px,p4.py), (0, 255, 0), 2)

        cv2.imshow("Eye",treshold_eye)
        cv2.imshow("Region 1 ",region1)
        cv2.imshow("Region 2",region2)
        cv2.imshow("Region 3 ",region3)
        cv2.imshow("Region 4",region4)
        


    
    #calculer les fps
    fps += 1
    sfps = fps / (time.time() - start_time)
    cv2.putText(frame, "FPS : " + str(int(sfps)), (10, 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    cv2.imshow("Frame",frame)
   
   

    key = cv2.waitKey(1)

    if key == 27:
        break

cap.release()

