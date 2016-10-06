#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Krawett
#
# Created:     04/10/2016
# Copyright:   (c) Krawett 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import os
import pygame
from random import randint

#Variables
pygame.init()
gameOver = False

#GameState
onGame = True
onPause = False

#Player
playerPosX = 10
playerPosY = 10

playerW = 35
playerH = 70

playerVelocity = 2

playerMoveUp = False
playerMoveDown = False
playerMoveLeft = False
playerMoveRight = False
playerIsWalking = False
playerRun = False

player = pygame.Rect(playerPosX, playerPosY,playerW, playerH)

#Objects


#Monsters

monsterPosX = 350
monsterPosY = 350
monsterW = 90
monsterH = 90
monsterDestX = 350
monsterDestY = 350

monster = pygame.Rect(monsterPosX, monsterPosY, monsterW, monsterH)

#===============================================================================
#Creation Fenetre===============================================================


game = pygame.display.set_mode((800,600))
pygame.display.set_caption("Jeu")


#===============================================================================
#Corps du jeu===================================================================

clock = pygame.time.Clock()

while not gameOver:
#EVENEMENTS=====================================================================
    if onGame:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOver = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:#HAUT
                    playerMoveUp = True
                if event.key == pygame.K_s:#BAS
                    playerMoveDown = True
                if event.key == pygame.K_a:#GAUCHE
                    playerMoveLeft = True
                if event.key == pygame.K_d:#DROITE
                    playerMoveRight = True
                if event.key == pygame.K_ESCAPE:#ECHAP | Quitte le jeu
                    gameOver = True
                if event.key == pygame.K_LSHIFT:#ECHAP | Quitte le jeu
                    playerRun = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:#HAUT
                    playerMoveUp = False
                if event.key == pygame.K_s:#BAS
                    playerMoveDown = False
                if event.key == pygame.K_a:#GAUCHE
                    playerMoveLeft = False
                if event.key == pygame.K_d:#DROITE
                    playerMoveRight = False
                if event.key == pygame.K_LSHIFT:#ECHAP | Quitte le jeu
                    playerRun = False

#UPDATE=========================================================================

    if playerMoveUp:#========================================================
        if playerRun:
            player.move_ip(0, -playerVelocity*2)#                           #
        else:
            player.move_ip(0, -playerVelocity)#                             #
    if playerMoveDown:                          #                           #
        if playerRun:
            player.move_ip(0, +playerVelocity*2)#                           #
        else:
            player.move_ip(0, +playerVelocity)#             DEPLACEMENT     #
    if playerMoveLeft:                          #             DU            #
        if playerRun:
            player.move_ip(-playerVelocity*2, 0)#           JOUEUR          #
        else:
            player.move_ip(-playerVelocity, 0)#                             #
    if playerMoveRight:                         #                           #
        if playerRun:
            player.move_ip(+playerVelocity*2, 0)#                           #
        else:
            player.move_ip(+playerVelocity, 0)#==============================

    #Deplacement monstre
    if monster.x < monsterDestX:
        monster.move_ip(1, 0)
    if monster.x > monsterDestX:
        monster.move_ip(-1, 0)
    if monster.y < monsterDestY:
        monster.move_ip(0, 1)
    if monster.y > monsterDestY:
        monster.move_ip(0, -1)
    elif monster.x == monsterDestX and monster.y == monsterDestY:
        monsterDestX = randint(350, 510)
        monsterDestY = randint(350, 510)

    #Affichage position monstre
    print()
    print("Destination: ",monsterDestX, " | ",monsterDestY )
    print("Position: ", monster.x, " | ", monster.y)



#DRAW===========================================================================
    game.fill((255,255,255))
    pygame.draw.rect(game, (255,0,0), player, 1)
    pygame.draw.rect(game, (5,0,0), monster, 2)
#===============================================================================
    pygame.display.update()#Rafraichissement de l'ecran
    clock.tick(30)#Taux d'image/secondes


pygame.quit()
quit()
