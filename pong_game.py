# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 17:13:46 2022

@author: atpax
"""
#used boiler plate code for initial structure. 

import pygame, sys, random
 
pygame.init()
 
WIDTH, HEIGHT = 1280, 720
 
FONT = pygame.font.SysFont("Consolas", int(WIDTH/20))
 
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong!")
CLOCK = pygame.time.Clock()

#Paddles

player = pygame.Rect(WIDTH-110, HEIGHT/2-50, 10,100)
opponent = pygame.Rect(110, HEIGHT/2-50, 10,100)
while True:
    keys_pressed = pygame.key.get_pressed()
    #player up motion
    if keys_pressed[pygame.K_UP]:
        if player.top>0:
            player.top -=2 #increaase y value goes down, reducing goes up) 
    #Player down motion
    if keys_pressed[pygame.K_DOWN]:
        if player.bottom<HEIGHT:
            player.bottom +=2
            
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    SCREEN.fill("black") #fills the screen with black colour after each action update. 
    pygame.draw.rect(SCREEN, "white", player)
    pygame.draw.rect(SCREEN, "white", opponent)
    pygame.display.update()
    CLOCK.tick(300)