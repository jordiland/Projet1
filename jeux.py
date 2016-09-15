#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      jordiland
#
# Created:     14/09/2016
# Copyright:   (c) jordiland 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import pygame
import time

pygame.init()

#Dimensions--------------------------------------------
largeurFenetre = 800
hauteurFenetre = 500

#Couleur-----------------------------------------------
rouge = (255,0,0)
marron = (150,60,60)
jaune = (255,255,0)
vert = (0,255,0)
bleu = (0,0,255)    #Arrache aussi les yeux !!
bleuMarine = (0,0,130)
violet = (130,0,255) # Arrache les yeux !!
rose = (255,0,130)

posX = 50
posY = 50

fenetre = pygame.display.set_mode((largeurFenetre, hauteurFenetre))
pygame.display.set_caption("Jeux")

img = pygame.image.load("Img/mario.png")
img = pygame.transform.scale(img, (75, 75))

#Creation de rectangle (pygame.Rect())
bouton1 = pygame.Rect(300, 350, 200, 50)
bouton2 = pygame.Rect(300, 410, 200, 50)

police = pygame.font.SysFont("arial" , 15)



def affImage(x,y,img):
    fenetre.blit(img,(x,y))


#def principale():  # fonction principale
#    x = 150
#    y = 200

game_over = False

#fonction pour repetee lapui sur une touche ( vitesse apuui, nombre de foi dapui)
pygame.key.set_repeat(1, 10)

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                if posX < 730:
                    posX += 2

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if posX > -10:
                    posX -= 2

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                if posY < 425:
                    posY += 2

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if posY > 0:
                    posY -= 2

        fenetre.fill(vert)

        #Affichage des rectangles
        pygame.draw.rect(fenetre, jaune, bouton1, 6)
        pygame.draw.rect(fenetre, rouge, bouton2, 6)

        affImage(posX,posY,img)
        pygame.display.update()

        #time.sleep(1)
        #fenetre.fill(jaune)
        #pygame.display.update()
        #time.sleep(1)
        #fenetre.fill(rouge)
        #pygame.display.update()
        #time.sleep(1)

#principale()
pygame.quit()
quit()
