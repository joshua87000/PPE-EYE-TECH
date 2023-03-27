
import time
from tkinter import *
from PIL import Image, ImageDraw, ImageFont
from PIL import Image, ImageTk

import screeninfo

# Récupérer la dimension de l'écran principal
ecran = screeninfo.get_monitors()[0]
largeur_ecran, hauteur_ecran = ecran.width, ecran.height

class FadeLabel(Label):
    def __init__(self, master, text, **kwargs):
        super().__init__(master, text=text, **kwargs)
        self.opacity = 0.0
        self.fade_in()

    def fade_in(self):
        self.opacity += 0.05
        if self.opacity > 1.0:
            return
        alpha = int((1 - self.opacity) * 255)
        self.config(fg=f"#{alpha:02x}{alpha:02x}{alpha:02x}")
        self.after(50, self.fade_in)




close = 0

def Agrandir(event):
    
    for i in range(100):
      root.geometry("{0}x100+200+100".format( 100 + 3*i))
      root.update_idletasks()
      time.sleep(0.0001)
    label.place(x=0, y=0)
    img2 = PhotoImage(file=r"C:\Users\Joshua\Downloads\youtubeLogo.png")

    label2 = Label(root, image=img2)
    label2.place(x=200, y=0)
    label2.pack()


    

def Gemini(event):
    img = Image.new('RGBA', (400, 200), (255, 29, 0, 0))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf", 100)
    draw.text((20,45), "GEMINI", font=font, fill=(0,0, 0, 128))


    canvas = Canvas(root, width=400, height=200)
    canvas.pack()
    image_tk = ImageTk.PhotoImage(img)
    canvas.create_image(0, 0, anchor=NW, image=image_tk)
    root.mainloop()

    

def ouverture():
    print("teer")
    positionFinal = (200,100)
    posistionActuel = ((int)(largeur_ecran/2 -200) ,  (int)(hauteur_ecran/2 -100))

    tailleFinal = (100,100)
    tailleActuel = (400,200)

    nmbStep = 10
    stepPostion = ((posistionActuel[0] - positionFinal[0])/nmbStep, (posistionActuel[1] - positionFinal[1])/nmbStep)
    stepTaille = ((tailleActuel[0] - tailleFinal[0])/nmbStep, (tailleActuel[1] - tailleFinal[1])/nmbStep)
    for i in range(nmbStep):

        posistionActuel = (posistionActuel[0] - stepPostion[0], posistionActuel[1] - stepPostion[1])
        tailleActuel = (tailleActuel[0] - stepTaille[0], tailleActuel[1] - stepTaille[1])

        root.geometry("{2}x{3}+{0}+{1}".format((int)(posistionActuel[0]), (int)(posistionActuel[1]),(int)(tailleActuel[0]), (int)(tailleActuel[1])))
        
        root.update_idletasks()
        time.sleep(0.01)

    LogoEye = PhotoImage(file=r"C:\Users\Joshua\Downloads\logoEye.png")
    
    label.config(image=LogoEye)
    label.image = LogoEye  
    root.bind('<Enter>', enter)
    root.bind('<Leave>', leave)
    
  
 

predX = -50
predY = -50
def deplacer_fenetre(event):
    global predX
    global predY
    if(predX != -50):
        root.geometry("+{0}+{1}".format(predX-50, predY-50))
        predX = event.x_root
        predY = event.y_root
    else:
        predX = event.x_root
        predY = event.y_root
       

# Créer une instance de la classe Tk pour la fenêtre principale
root = Tk()

# Créer une instance de la classe Toplevel pour la fenêtre sans barre de titre


root.geometry("400x200+{0}+{1}".format((int)(largeur_ecran/2 -200) , (int)(hauteur_ecran/2 -100)))
root.overrideredirect(True)
root.attributes("-topmost", True)



label = FadeLabel(root, "Gemini", font=("Helvetica", 55))
label.pack(expand=True, fill=BOTH)



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


root.after(3000, ouverture)


root.bind('<Escape>', lambda event: root.quit())
root.bind('k', Gemini)
root.bind("<B1-Motion>", deplacer_fenetre)
root.bind('t',Agrandir)


# Afficher la fenêtre
root.mainloop()

