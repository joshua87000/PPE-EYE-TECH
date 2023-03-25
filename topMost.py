import cv2
import tkinter as tk
import threading
from tkinter import *
from tkinter.ttk import *
import time
import win32gui
import drawCV2 as dC
import dlib
import time
import pyautogui
import subprocess


def recherche_chaine(chaine1, chaine2):
    if chaine1 in chaine2:
        return 1
    else:
        return 0

# fonction pour créer la fenêtre OpenCV
def openCV_window():

    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor(r"C:\Users\Joshua\Desktop\PPE EYE TECH\shape_predictor_68_face_landmarks.dat")

    cap = cv2.VideoCapture(1)

    fps = 0
    start_time = time.time()

    temps1L = time.time()
    doubleCloseL = 0

    temps1R = time.time()
    doubleCloseR = 0
    open = 0
    count = 0
    timeTurn = time.time()
    turnLeft = 0
    minTurn = 100
    maxTurn = 0

    cmp = 0
    mode = 0

    while True:
        _, frame = cap.read()

        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)


        faces = detector(gray)

        
        
    
        for face in faces:
            
            x, y = face.left() , face.top()
            x1 ,y1 = face.right(), face.bottom()
        
            landmarks = predictor(gray,face)

            p1L = dC.Point(landmarks,37)
            p2L = dC.Point(landmarks,38)
            p3L = dC.Point(landmarks,41)
            p4L = dC.Point(landmarks,40)

            p1R = dC.Point(landmarks,43)
            p2R = dC.Point(landmarks,44)
            p3R = dC.Point(landmarks,47)
            p4R = dC.Point(landmarks,46)

            scale1 = dC.Point(landmarks,27)
            scale2 = dC.Point(landmarks,28)

            scale = dC.distance_entre_points(scale1,scale2)

            midHautL = dC.Point.fromcoord(int((p1L.px + p2L.px)/2), int((p1L.py + p2L.py)/2),landmarks,0)
            midBasL = dC.Point.fromcoord(int((p3L.px + p4L.px)/2), int((p3L.py + p4L.py)/2),landmarks,0)

            midHautR = dC.Point.fromcoord(int((p1R.px + p2R.px)/2), int((p1R.py + p2R.py)/2),landmarks,0)
            midBasR = dC.Point.fromcoord(int((p3R.px + p4R.px)/2), int((p3R.py + p4R.py)/2),landmarks,0)

            noz = dC.Point(landmarks,33)

            mouthL = dC.Point(landmarks,48)
            mouthR = dC.Point(landmarks,54)

            mouthTop = dC.Point(landmarks,51)
            mouthBot = dC.Point(landmarks,57)

            ratioMouth = dC.distance_entre_points(mouthL,mouthR)/scale

            dC.draw_line_between_points(dC.Point(landmarks,31),dC.Point(landmarks,2),frame)
            dC.draw_line_between_points(dC.Point(landmarks,35),dC.Point(landmarks,14),frame)

            ratioNozL =dC.distance_entre_points(mouthL,noz)/dC.distance_entre_points(midHautL,midBasL)
            
            for i in range(68):
                P = dC.Point(landmarks,i)
                cv2.circle(frame,(P.px,P.py),3,(0, 0, 255),1)

            PgaucheL = dC.Point(landmarks,36)
            PdroiteL = dC.Point(landmarks,39)

            PgaucheR = dC.Point(landmarks,42)
            PdroiteR = dC.Point(landmarks,45)

            visageHaut = dC.Point(landmarks,19)

            grosYeuxL = dC.distance_entre_points(dC.Point(landmarks,41),dC.Point(landmarks,19))/dC.distance_entre_points(dC.Point(landmarks,20),dC.Point(landmarks,19))
            grosYeuxD = dC.distance_entre_points(dC.Point(landmarks,46),dC.Point(landmarks,24))/dC.distance_entre_points(dC.Point(landmarks,23),dC.Point(landmarks,24))
            grosYeux = (grosYeuxD + grosYeuxL)/2

            print(grosYeux)

            if(grosYeux > 2.8):
                if(mode == 0):
                    print("Big eye")
                elif(mode == 1):
                    pyautogui.press('k')

            ratioTurn = dC.distance_entre_points(dC.Point(landmarks,31),dC.Point(landmarks,2))/dC.distance_entre_points(dC.Point(landmarks,35),dC.Point(landmarks,14))
            #print(ratioTurn)

            if ratioTurn < 0.5 and turnLeft == 0:
                turnLeft = 1
                timeTurn = time.time()
                print("detect")
                minTurn = 100
            elif(turnLeft == 1):
                if(minTurn > ratioTurn):
                    minTurn = ratioTurn
                if ratioTurn > minTurn + 0.1 :
                    turnLeft = 0
                    print("LEEEFt")
                    if(mode == 0):
                        pyautogui.hotkey('ctrl', 'tab')
                    elif(mode == 1):
                        pyautogui.press('l')

                if(time.time() - timeTurn) > 0.4:
                    print("annule : "+ str (ratioTurn))
                    turnLeft = -1



            if ratioTurn > 2 and turnLeft == 0:
                turnLeft = 2
                timeTurn = time.time()
                print("detect")
                maxTurn = 0
            elif(turnLeft == 2):
                if(maxTurn < ratioTurn):
                    maxTurn = ratioTurn
                if ratioTurn < maxTurn - 0.1 :
                    turnLeft = 0
                    print("RIGGHT")
                    if(mode == 0):
                        pyautogui.hotkey('ctrl', 'shift', 'tab')
                    elif (mode == 1):
                        pyautogui.press('j')

                if(time.time() - timeTurn) > 0.4:
                    print("annule : "+ str (ratioTurn))
                    turnLeft = -1

            if(turnLeft == -1):
                if(ratioTurn > 0.8 and ratioTurn < 1.5):
                    turnLeft = 0
                    print("réinit: " + str(ratioTurn))

        


            ratioL = dC.distance_entre_points(PgaucheL,PdroiteL)/dC.distance_entre_points(midHautL,midBasL)
            ratioR = dC.distance_entre_points(PgaucheR,PdroiteR)/dC.distance_entre_points(midHautR,midBasR)


        

            if ((ratioL+ratioR)/2) > 6:
                cv2.putText(frame, "blinkL", (300, 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                if(doubleCloseL == 0):
                    time1L = time.time()
                    doubleCloseL = 1

                elif(doubleCloseL == 2):
                    difference = time.time()-time1L
                    print("double")
                    doubleCloseL = 3

                    if(mode == 0):
                        pyautogui.hotkey('ctrl', 't')
                    

                    
                    
            else:
                if(doubleCloseL == 1):
                    doubleCloseL = 2
                elif(doubleCloseL == 3):
                    doubleCloseL = 0
                    
            if(doubleCloseL == 2 and (time.time() - time1L) > 0.5):
                doubleCloseL = 0
                print("simple L - ")
                print(time.time() - time1L)
        

                
    
                


        cv2.imshow("image",frame)
        key = cv2.waitKey(1)


        if key == 27:
            print("end")
            break

        cmp=cmp+1
        if cmp == 30:
            print("Change")
            cmp = 0
            window = win32gui.GetForegroundWindow()
            window_title = win32gui.GetWindowText(window)
        
            
            if recherche_chaine("YouTube", window_title) == 1:
                mode = 1
            elif recherche_chaine("Netflix", window_title) == 1:
                mode = 2
            else:
                mode = 0
                
            



            



    cap.release()

# fonction pour créer la fenêtre Tkinter

def tkinter_window():
    root = Tk()
    root.title("Ma fenêtre")

    width = 300
    height = 130
    root.geometry("%dx%d" % (width, height))
    root.attributes('-alpha', 0.5)

    root.attributes("-topmost", True)

    LogoYoutube = PhotoImage(file=r"C:\Users\Joshua\Downloads\youtubeLogo.png")
    LogoChrome = PhotoImage(file=r"C:\Users\Joshua\Downloads\logoChrome.png")
    LogoNetflix = PhotoImage(file=r"C:\Users\Joshua\Downloads\logoNetflix.png")
    
    image = LogoChrome
    label = Label(root, image=image)
    label.pack()

    root.update()  # mise à jour de la fenêtre

    duration = 250

    def enter(event):
        current_opacity = root.attributes('-alpha')
        target_opacity = 1.0
        opacity_difference = target_opacity - current_opacity
        frames = int(duration / 20)
        opacity_increment = opacity_difference / frames
        
        for i in range(frames):
            opacity = current_opacity + opacity_increment * i
            root.attributes('-alpha', opacity)
            root.update_idletasks()
            time.sleep(duration / frames / 1000)



    def leave(event):
        
        current_opacity = root.attributes('-alpha')
        target_opacity = 0.5
        opacity_difference = target_opacity - current_opacity
        frames = int(duration / 20)
        opacity_increment = opacity_difference / frames
        
        for i in range(frames):
            opacity = current_opacity + opacity_increment * i
            root.attributes('-alpha', opacity)
            root.update_idletasks()
            time.sleep(duration / frames / 1000)


    
    def update_App():
        nonlocal image
        window = win32gui.GetForegroundWindow()
        window_title = win32gui.GetWindowText(window)
    
        
        if recherche_chaine("YouTube", window_title) == 1:
            image = LogoYoutube
        elif recherche_chaine("Netflix", window_title) == 1:
            image = LogoNetflix
        else:
            image = LogoChrome
    
        label.configure(image=image)
        label.image = image  # mise à jour de l'image du Label
    
        root.after(2000, update_App)
    
    update_App()

    root.bind('<Enter>', enter)
    root.bind('<Leave>', leave)

    root.mainloop()




# créer un thread pour la fenêtre OpenCV
openCV_thread = threading.Thread(target=openCV_window)
openCV_thread.start()

# créer un thread pour la fenêtre Tkinter
tkinter_thread = threading.Thread(target=tkinter_window)
tkinter_thread.start()
