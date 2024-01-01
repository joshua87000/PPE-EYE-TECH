import pygame
import math
import time

from typing import List, Tuple

class Chare:
    def __init__(self):
        self.lettre = None
        self.After = [(0, chr(i + 97)) for i in range(26)] + [(0, " "), (0, "'")]
        self.iteration = 0

    def set_lettre(self, add: str):
        self.lettre = add

    def get_iteration(self):
        return self.iteration

    def add_lettre(self, ant: str):
        index = 26 if ant == ' ' else 27 if ant == "'" else ord(ant) - 97
        self.iteration += 1
       # print(index)
        #print(ant)
        if index > 0:
            self.After[index] = (self.After[index][0] + 1, self.After[index][1])

    def trier_result(self):
        self.After.sort(key=lambda x: x[0], reverse=True)

    def afficher_stat(self):
        total = 0
       #self.After = [tuple for tuple in self.After if tuple[1] != ' ']
        print(f"Lettre: {self.lettre}")
        print(self.iteration)
        if self.iteration > 0:
            for i in range(28):
                apparition = (self.After[i][0] / self.iteration) * 100
                total += apparition
                self.After[i] = (apparition, self.After[i][1])
                print(f"({self.After[i][1]}) - {apparition:.2f}   {total:.2f}")


def recupData(C):
  with open(r"C:\Users\Joshua\Desktop\PPE EYE TECH\t.txt", "r") as ifs:
    c = ifs.read(1)

    alphabet = "abcdefghijklmnopqrstuvwxyz '"
    for i in range(28):
      C[i].set_lettre(alphabet[i])

    for i in range(3130):
      c2 = ifs.read(1)

      x = 26 if c == " " else 27 if c == "'" else ord(c) - 97
      C[x].add_lettre(c2)
      c = c2

    for i in range(28):
      C[i].trier_result()
      C[i].afficher_stat()



 
      
C = [Chare() for i in range(28)]
recupData(C)





pygame.init()

font = pygame.font.Font(None, 45)

window_size = (500, 500)
screen = pygame.display.set_mode(window_size)

def draw_cercle(screen, posX ,posY,L):
    screen.fill((255, 255, 255))

    pygame.draw.circle(screen, (0,0, 0), (posX, posY), 200,2)

  
    pygame.draw.line(screen, (255, 0, 0), 
                     (posX + (-math.sqrt(2) / 2) * 200, posY - (math.sqrt(2) / 2) * 200), 
                     (posX - (-math.sqrt(2) / 2) * 200, posY + (math.sqrt(2) / 2) * 200), 5)
    pygame.draw.line(screen, (255, 0, 0), 
                     (posX + (math.sqrt(2) / 2) * 200, posY - (math.sqrt(2) / 2) * 200), 
                     (posX + (-math.sqrt(2) / 2) * 200, posY + (math.sqrt(2) / 2) * 200), 5)

   
    pygame.draw.circle(screen, (0,0,0), (posX, posY), 100,2)
    pygame.draw.circle(screen, (255,255,255), (posX, posY),99)

    screen.blit(L[0], (posX-12,posY-160))
    screen.blit(L[1], (posX+140,posY-12))
    screen.blit(L[2], (posX-12,posY+140))   
    screen.blit(L[3], (posX-160,posY-12))

def getSuiavnt(step,lettre,C):
    for i in range(28):
        if lettre == C[i].lettre :
            return C[i].After[0+4*step][1] , C[i].After[1+4*step][1] , C[i].After[2+4*step][1] , C[i].After[3+4*step][1]
        


    



px = 250
py = 220
etat = 0
step =0

last = ' '
t1,t2,t3,t4 = getSuiavnt(step,last,C)
L1 = font.render(t1, True, (0, 0, 0))
L2 = font.render(t2, True, (0, 0, 0))
L3 = font.render(t3, True, (0, 0, 0))
L4 = font.render(t4, True, (0, 0, 0))




txt =" "

font2 = pygame.font.Font(None,30)
text = font2.render(txt, True, (0, 0, 0))
text_rect = text.get_rect()
text_rect.center = (px,py)

lettre = [L1,L2,L3,L4]

def animation(pos,etat):
    if etat == 1:
        pos[0] += 5
    if(pos[0]>750):
        pos[0] = -250
    if(pos[0] == 250):
        etat = 0
    return pos,etat

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                etat = 1
                step += 1
                t1,t2,t3,t4 = getSuiavnt(step,last,C)
                L1 = font.render(t1, True, (0, 0, 0))
                L2 = font.render(t2, True, (0, 0, 0))
                L3 = font.render(t3, True, (0, 0, 0))
                L4 = font.render(t4, True, (0, 0, 0))
            if event.key == pygame.K_RETURN:
                print(txt)
                step = 0
                txt = " "
                last = ' '
                text = font2.render(txt, True, (0, 0, 0))
                text_rect = text.get_rect()
                text_rect.center = (px,py)
                t1,t2,t3,t4 = getSuiavnt(step,last,C)
                L1 = font.render(t1, True, (0, 0, 0))
                L2 = font.render(t2, True, (0, 0, 0))
                L3 = font.render(t3, True, (0, 0, 0))
                L4 = font.render(t4, True, (0, 0, 0))
            if event.key == pygame.K_RIGHT:
                step = 0
                txt = txt + t2
                text = font2.render(txt, True, (0, 0, 0))
                text_rect = text.get_rect()
                text_rect.center = (px,py)
                last = t2
                t1,t2,t3,t4 = getSuiavnt(step,last,C)
                L1 = font.render(t1, True, (0, 0, 0))
                L2 = font.render(t2, True, (0, 0, 0))
                L3 = font.render(t3, True, (0, 0, 0))
                L4 = font.render(t4, True, (0, 0, 0))
            if event.key == pygame.K_DOWN:
                step = 0
                txt = txt + t3
                text = font2.render(txt, True, (0, 0, 0))
                text_rect = text.get_rect()
                text_rect.center = (px,py)
                last = t3
                t1,t2,t3,t4 = getSuiavnt(step,last,C)
                L1 = font.render(t1, True, (0, 0, 0))
                L2 = font.render(t2, True, (0, 0, 0))
                L3 = font.render(t3, True, (0, 0, 0))
                L4 = font.render(t4, True, (0, 0, 0))
            if event.key == pygame.K_UP:
                step = 0
                txt = txt + t1
                text = font2.render(txt, True, (0, 0, 0))
                text_rect = text.get_rect()
                text_rect.center = (px,py)
                last = t1
                t1,t2,t3,t4 = getSuiavnt(step,last,C)
                L1 = font.render(t1, True, (0, 0, 0))
                L2 = font.render(t2, True, (0, 0, 0))
                L3 = font.render(t3, True, (0, 0, 0))
                L4 = font.render(t4, True, (0, 0, 0))
            if event.key == pygame.K_LEFT:
                step = 0
                txt = txt + t4
                text = font2.render(txt, True, (0, 0, 0))
                text_rect = text.get_rect()
                text_rect.center = (px,py)
                last = t4
                t1,t2,t3,t4 = getSuiavnt(step,last,C)
                L1 = font.render(t1, True, (0, 0, 0))
                L2 = font.render(t2, True, (0, 0, 0))
                L3 = font.render(t3, True, (0, 0, 0))
                L4 = font.render(t4, True, (0, 0, 0))
            if event.key == pygame.K_DELETE:
                step = 0 
                txt = txt[:1]
                last = txt[-1]
                text = font2.render(txt, True, (0, 0, 0))
                text_rect = text.get_rect()
                text_rect.center = (px,py)
                t1,t2,t3,t4 = getSuiavnt(step,last,C)
                L1 = font.render(t1, True, (0, 0, 0))
                L2 = font.render(t2, True, (0, 0, 0))
                L3 = font.render(t3, True, (0, 0, 0))
                L4 = font.render(t4, True, (0, 0, 0))




               
                
    lettre = [L1,L2,L3,L4]  
    pos,etat = animation([px,py],etat)
    px,py = pos
    draw_cercle(screen, px, py,lettre)
    screen.blit(text, text_rect)



    

   
    pygame.display.update()


pygame.quit()
