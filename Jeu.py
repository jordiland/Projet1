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

pygame.init()

#Dimensions--------------------------------------------
largeurFenetre = 800
hauteurFenetre = 500

#Couleur-----------------------------------------------
marron = (150,60,60)
vert = (0,255,0)
bleu = (0,0,255)    #Arrache aussi les yeux !!
bleuMarine = (0,0,130)
violet = (130,0,255) # Arrache les yeux !!
rose = (255,0,130)



fenetre = pygame.display.set_mode((largeurFenetre, hauteurFenetre))
pygame.display.set_caption("Jeux")



game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    fenetre.fill(marron)
    pygame.display.update()

pygame.quit()
quit()
