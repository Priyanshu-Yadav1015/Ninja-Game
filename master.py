import os
import sys
import math
import random
import pygame
from Buttons import ScaledButton
from Level import level, levels
import time


class Master:
    def __init__(self):
        pygame.init()
    def run(self):                
        clock = pygame.time.Clock()
        fps = 60

        screen_width = 320*2
        screen_height = 240*2

        screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption('Platformer')


        start_img = pygame.image.load('img/start_btn.png')
        exit_img = pygame.image.load('img/exit_btn.png')

        start_button = ScaledButton(screen_width // 2 , screen_height // 2 -100, start_img)
        exit_button = ScaledButton(screen_width // 2, screen_height // 2  +100, exit_img)

        present="main_menu"
        run = True
        while run:
            clock.tick(fps)
            screen.fill((207, 188, 223))
            if present=="main_menu":
                if start_button.draw(screen):
                    present="level_selector"
                    loading=True
                    time.sleep(0.2)
                if exit_button.draw(screen):
                    run = False
            elif present=="level_selector":
                screen.fill((202, 182, 205))
                for level in levels:
                    level.draw(screen)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            for i in levels:
                                i.state+=1
                                if i.state==len(levels)-1:
                                    i.state=-1
                        if event.key == pygame.K_RIGHT:
                            for i in levels:
                                i.state-=1
                                if i.state==-2:
                                    i.state=len(levels)-2
            elif present=="game":
                pass

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        main_menu = True
            pygame.display.update()

Master().run()