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

boutonSelect = 1

vie = 100
force = 10
intel = 10
agi = 1


#Etat----------------------------------------------

onMenu = True
onJouer = False
onOption = False


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
gris = (240, 240, 240)


posX = 50
posY = 50


def affImage(x,y,img):
    fenetre.blit(img,(x,y))

fenetre = pygame.display.set_mode((largeurFenetre, hauteurFenetre))
pygame.display.set_caption("Jeux")

img = pygame.image.load("Img/mario.png")
img = pygame.transform.scale(img, (75, 75))

#Creation de rectangle (pygame.Rect())----------------------
bouton1 = pygame.Rect(300, 350, 200, 50)
bouton2 = pygame.Rect(300, 410, 200, 50)
cadrestate = pygame.Rect(1, 448, 300, 50)

# creation Hitbox--------------------------------------------
HitboxPerso = pygame.Rect(60, 50, 55,75)


# boulefeu--------------------------------------------------
boule = pygame.Rect(posX ,posY ,10,10)
boule2 = pygame.Rect(posX,posY,10,10)


#Creation texte---------------------------------------------
petitePolice = pygame.font.SysFont("arial", 12)
police = pygame.font.SysFont("comic" , 35)
texte = police.render("Jouer",1, bleu)
texteBouton1 = police.render("Option",1, bleu )
texteNomjeu = police.render("Jordiland",1,jaune)
textetir = police.render("apui_sur__t__et_apui_sur_r",1,bleu)
texteStats = petitePolice.render("Vie: |"+ str(vie) +"| Force: |"+ str(force) +"| Intelligence: |" +str(intel)+ "| Agilite: |" +str(agi)+"|", 1, bleu)



game_over = False

#fonction pour repetee lapui sur une touche ( vitesse apuui, nombre de foi dapui)
pygame.key.set_repeat(1, 10)

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:

            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                print pygame.event.event_name
                if posX < 730:
                    posX += 2
                    HitboxPerso = HitboxPerso.move(2,0)
                    boule = boule.move(2,0)





        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print pygame.event.get()
                if posX > -10:
                    posX -= 2
                    HitboxPerso = HitboxPerso.move(-2,0)
                    boule = boule.move(-2,0)





        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                print pygame.event.get()
                if posY < 425:
                    posY += 2
                    HitboxPerso = HitboxPerso.move(0,2)
                    boule = boule.move(0,2)


        if event.type == pygame.KEYDOWN:
            print pygame.event.get()
            if event.key == pygame.K_UP:
                if posY > 0:
                    posY -= 2
                    HitboxPerso = HitboxPerso.move(0,-2)
                    boule = boule.move(0,-2)


#tir--boule-----------------------------------
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_t:
                    boule = boule.move(100,0)


#-----re_affichageboule------------------------------------------
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                boule = pygame.Rect(posX ,posY ,10,10)


#---------------------------------------------------------------


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                Menu = False
                Option = False
                Jouer = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                onMenu = True
                onOption = False
                onJouer = False

            if event.key == pygame.K_o:
                onMenu = False
                onOption = True
                onJouer = False


            if event.key == pygame.K_RETURN:
                if boutonSelect == 1:
                    onMenu = False
                    onOption = False
                    onJouer = True


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                boutonSelect = 2
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                boutonSelect = 1



        if boutonSelect == 1:
            couleurBouton1 = bleu
            couleurBouton2 = jaune
        if boutonSelect == 2:
            couleurBouton1 = jaune
            couleurBouton2 = bleu








        if onMenu == True:
            fenetre.fill(vert)
            pygame.draw.rect(fenetre, couleurBouton1, bouton1, 6)
            pygame.draw.rect(fenetre, couleurBouton2, bouton2, 6)
            fenetre.blit(texte, (370, 365))
            fenetre.blit(texteBouton1, (357, 425))
            fenetre.blit(texteNomjeu, (350, 50))
            fenetre.blit(texteBouton1, (357, 425))
            fenetre.blit(texteNomjeu, (350, 50))

            #affImage(posX,posY,img,)
            pygame.display.update()

        if onOption == True:
            fenetre.fill(marron)
            pygame.display.update()

        if onJouer == True:
            fenetre.fill(gris)

            fenetre.blit(textetir, (300, 50))
            fenetre.blit(texteStats, (10, 450))

            pygame.draw.rect(fenetre, rouge, HitboxPerso, 2)
            pygame.draw.rect(fenetre, vert, boule, 10)
            pygame.draw.rect(fenetre, rouge, cadrestate, 6)

            affImage(posX,posY,img)
            pygame.display.update()


        #Affichage des rectangles


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
