import numpy as np
from math import *
import pygame
import sys
from pygame.locals import*
import random as rd

def pluspetity(a):
    cpt=1
    for i in range(1,10):
        if a[i]<a[i-1]:
            cpt=i
    return cpt


def genere_coo(a,b):
    bombe_x=[]
    bombe_y=[]
    for i in range(0,10):
        bombe_x+=[rd.randint(0,1000)]
        bombe_y+=[rd.randint(a,b)]
        
    return bombe_x,bombe_y
def sauvegarde(record):
    fichier = open("/home/seisen/Bureau/save", "w") 
    fichier.write(record) 
    fichier.close()
def lecture_sauvegarde():
    fichier = open("/home/seisen/Bureau/save", "r")
    contenu_sauvegarde=fichier.read()
    fichier.close()
    return contenu_sauvegarde
def hitbox(x,y,x1,y1):
    liste_hitbox=[]
    for i in range (0,10):
        liste_hitbox+=[x[i]+25]
        liste_hitbox+=[y[i]+25]
    for i in range (0,10):
        liste_hitbox+=[x1[i]+25]
        liste_hitbox+=[y1[i]+25]
    return liste_hitbox
def se_fait_toucher(x,y):
    touché=False
    for i in range(0,40,2):
        
        if x+25>(liste_hitbox[i]-25) and x+25<(liste_hitbox[i]+25) and y+25>(liste_hitbox[i+1]-25)and y+25<(liste_hitbox[i+1]+25):
            touché=True
            
        
    return touché 


record=lecture_sauvegarde()

pygame.init()
screen=pygame.display.set_mode((1000,800))
run=True


asteroide = pygame.image.load('img/asteroi.png')
fond = pygame.image.load('img/fond.jpg')
vessel= pygame.image.load('img/vessel.png')
white= [250,250,250]
screen.blit(fond,(0,0))
black=[0,0,0]
u=[222,137,78]
bombe_x=[]
bombe_y=[]

bombe_x,bombe_y=genere_coo(-800,0)
cpt=pluspetity(bombe_y)
bombe_x1,bombe_y1=genere_coo(-1600,800)
cpt1=pluspetity(bombe_y1)  
x=500
y=600
x1=800
y1=10
clock = pygame.time.Clock()
fps=30
compteur=0
color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')
font=pygame.font.Font(None, 50)


r=0
g=0
b=0

red=[250,0,0]
text1 = font.render("RECORD : "+record,1,(color_inactive))
record_saved=False
font=pygame.font.Font(None, 32)
text6= font.render("Entrez votre nom ",1,(color_inactive))
jeu_en_cour=2
input_box = pygame.Rect(400, 500, 300, 32)

color = color_inactive
active = False
text = ''
joueur=''
c_max_atteint=False
c=0
TpsZero = pygame.time.get_ticks()
while run:
    clock.tick(fps)
    
    for event in pygame.event.get():
        
            if event.type == pygame.QUIT:
                run=False
                pygame.quit()
    if jeu_en_cour==1:
        
        
        keys = pygame.key.get_pressed()
        screen.blit(fond,(0,0))
        
        
        if keys[pygame.K_DOWN]:
            if y<770:
                y+=15
            screen.blit(fond,(0,0))
        elif keys[pygame.K_UP]:
            if y>16:
                y-=15
            screen.blit(fond,(0,0))
        elif keys[pygame.K_LEFT]:
            if x>16:
               x-=15
            screen.blit(fond,(0,0))
        elif keys[pygame.K_RIGHT]:
            if x<960:
                x+=15
            screen.blit(fond,(0,0))
        elif bombe_y[cpt]>1000:  
            bombe_x,bombe_y=genere_coo(-800,0)
            cpt=pluspetity(bombe_y)    
        elif bombe_y1[cpt1]>1000:
            bombe_x1,bombe_y1=genere_coo(-1600,-800)
            cpt1=pluspetity(bombe_y1)  
            
            compteur+=3
        for i in range(0,10):
        
            screen.blit(asteroide,(bombe_x[i],bombe_y[i]))
            screen.blit(asteroide,(bombe_x1[i],bombe_y1[i]))
            
            if compteur<20:
                bombe_y[i]+=10+compteur
                bombe_y1[i]+=10+compteur
            else:
                bombe_y[i]+=26
                bombe_y1[i]+=26
        
        liste_hitbox=hitbox(bombe_x1,bombe_y1,bombe_x,bombe_y)
        touhé=se_fait_toucher(x,y)
        
        if touhé:
            if not record_saved:
                if int(record[0:4])<compteur*10:
                    sauvegarde(str(compteur*10)+" de "+joueur)
                    record_saved=True   
            
            jeu_en_cour=3
        

        font=pygame.font.Font(None, 50)
        text2 = font.render("SCORE : "+str(compteur*10),1,(color_inactive))
        screen.blit(vessel,(x,y))
        screen.blit(text2, (750, 10))
        screen.blit(text1, (10,750))
        
        pygame.display.flip()

    #________________________________MENU______________________________________________

    elif jeu_en_cour==2:
        
        if r!=250 and b==0 and g==0:
            r+=10
        elif b!=250 and r!=0 and g==0:
            b+=10
            r-=10
        elif b!=0 and r==0 and g!=250:
            g+=10
            b-=10
        elif g!=0 and b==0:
            g-=10
        arc_en_ciel=[r,g,b]
        font = pygame.font.Font(None, 150)
        text3=  font.render("BIENVENUE ",1,(arc_en_ciel))
        text4=  font.render(" SUR  ",1,(arc_en_ciel))
        text5=  font.render("FRANKLIN GAME ",1,(arc_en_ciel))
        font = pygame.font.Font(None, 110)
        if c>230:
            c_max_atteint=True 
        elif c<20:
            c_max_atteint=False
        if  c_max_atteint ==False:
            c+=15

        elif c_max_atteint:
            c-=15
        
        blancnoir = [c,c,c]
        text11=  font.render("PRESS ",1,(blancnoir))
        text12=  font.render("ENTER",1,(blancnoir))
        font=pygame.font.Font(None, 32)


        screen.blit(fond,(0,0))
        

        if event.type == pygame.MOUSEBUTTONDOWN:
               
            if input_box.collidepoint(event.pos):
               
                active = not active
            else:
                active = False
            pygame.time.delay(200)
            
            color = color_active if active else color_inactive
        
        if event.type == pygame.KEYDOWN:
            
            if active:
                if event.key == pygame.K_RETURN:
                    joueur=text
                    text = ''
                    jeu_en_cour=1
                elif event.key == pygame.K_BACKSPACE:
                    

                    text = text[:-1]
                else:
                    TpsUn = pygame.time.get_ticks()
                    if TpsUn-TpsZero>100:
                        text += event.unicode
                        TpsZero = pygame.time.get_ticks()
            
        txt_surface = font.render(text, True, color)
        
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width

        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))

        pygame.draw.rect(screen, color, input_box, 2)

        screen.blit(text3, (220,10))
        screen.blit(text4, (380,100))
        screen.blit(text5, (50,200))
        screen.blit(text6, (405,470))
        screen.blit(text11, (375,600))
        screen.blit(text12, (367,670))

        
        pygame.display.flip()
    else:
         
        pygame.display.flip()
        
