import cv2
import numpy as np
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

def onMouseClick(event, x, y, flags, param,add):
    if event == cv2.EVENT_LBUTTONUP:
        print(add)

def distance_entre_points(point1, point2):
    distance = math.sqrt((point2.px - point1.px)**2 + (point2.py - point1.py)**2)
    return distance

def draw_line_between_points(point1, point2, frame, color=(0, 255, 0), thickness=2):
    cv2.line(frame, (point1.px, point1.py), (point2.px, point2.py), color, thickness)


def draw_point(point,frame):
    cv2.circle(frame, (point.px, point.py), 5, (0, 0, 255), -1)


def draw_polyline(point_list, frame):
   points = np.array([[p.px, p.py] for p in point_list], dtype=np.int32)
   cv2.polylines(frame, points, isClosed=False, color=(0, 0, 255), thickness=2)
