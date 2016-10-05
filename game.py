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

monsterPosX = 500
monsterPosY = 200
monsterW = 90
monsterH = 90

monster = pygame.Rect(100, 100, monsterW, monsterH)

#===============================================================================
#Creation Fenetre===============================================================


game = pygame.display.set_mode((800,600))
pygame.display.set_caption("Jeu")


#===============================================================================
#Corps du jeu===================================================================

clock = pygame.time.Clock()

while not gameOver:
#EVENEMENTS=====================================================================
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

    monster.move_ip(0, 1)
#DRAW===========================================================================
    game.fill((255,255,255))
    pygame.draw.rect(game, (255,0,0), player, 1)
    pygame.draw.rect(game, (5,0,0), monster, 2)
#===============================================================================
    pygame.display.update()#Rafraichissement de l'ecran
    clock.tick(30)#Taux d'image/secondes


pygame.quit()
quit()
