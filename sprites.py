# sprite classes for game

import pygame as pg
from pygame.sprite import Sprite
import random
from settings import *
from time import sleep

class Player(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = pg.Surface((17,73))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH*11/12, HEIGHT/2)
        # self.image1 = pg.Surface((17,73))
        # self.image1.fill(WHITE)
        # self.rect1 = self.image1.get_rect()
        # self.rect1.center = (WIDTH*6/12, HEIGHT/2)
        self.vx = 0
        self.vy = 0
        self.falling = False
        self.max_velocity = -25
        self.up = pg.K_UP
        self.down = pg.K_DOWN

        # self.line = pg.Surface((10,480))
        # self.line.fill(WHITE)
        # self.center_line = self.image.get_rect()
        # self.center_line.center = (WIDTH*5/2, HEIGHT/2)
        self.central_line = pg.Rect(WIDTH/2, 10, 1, HEIGHT)
    def update(self):
        self.vy = 0
        self.vx = 0
        # self.gravity()
        keys = pg.key.get_pressed()
        if keys[self.up]:
            self.vy = -15
        if keys[self.down]:
            self.vy = 15
        if keys[pg.K_BACKSPACE]:
            pg.quit()
        # if keys[pg.K_UP] and self.falling == False:
        #     self.jump()  

        # self.rect.x += self.vx
        self.rect.y += self.vy
    def gravity(self):
        if self.rect.x < HEIGHT-40:
            self.falling = True
            self.vx -= 10
        elif self.rect.x >= HEIGHT: 
            self.falling = False
            self.vx = 120
            self.rect.x = HEIGHT-10
    # def borders(self):
    #     if self.rect.x == WIDTH:
    #         self.vx = 0

class Object(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = pg.Surface((5,HEIGHT))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH*6/12, HEIGHT/2)

class Ball(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = pg.Surface((15,15))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH*6/12, HEIGHT/2)

