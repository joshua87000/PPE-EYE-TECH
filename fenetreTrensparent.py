from tkinter import *
from tkinter.ttk import *
import time
import win32gui

def recherche_chaine(chaine1, chaine2):
    if chaine1 in chaine2:
        return 1
    else:
        return 0


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
   
    global LogoYoutube
    global LogoChrome
    global LogoNetflix

    window = win32gui.GetForegroundWindow()
    window_title = win32gui.GetWindowText(window)
   
    print(window_title)
    if(recherche_chaine("YouTube",window_title) == 1):
         label.configure(image=LogoYoutube)
    elif recherche_chaine("Netflix",window_title) == 1:
         label.configure(image=LogoNetflix)
    else:
        label.configure(image=LogoChrome)

   
    root.after(2000, update_App)


update_App()


root.bind('<Enter>', enter)
root.bind('<Leave>', leave)

root.mainloop()
