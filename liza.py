{\rtf1\ansi\ansicpg1251\cocoartf2761
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import random\
import pygame\
\
pygame.init()\
win = pygame.display.set_mode((450, 450))\
win.fill((0, 0, 0))\
\
\
class Board:\
    def __init__(self, surface):\
        self.surface = surface\
        self.x1 = 175\
        self.y1 = 225\
        self.x2 = 275\
        self.y2 = 225\
\
    def draw_line(self, width):\
        pygame.draw.line(win, 'white', (self.x1, self.y1), (self.x2, self.y2), 3)\
\
    def move_by_keys(self):\
        keys = pygame.key.get_pressed()\
        if keys[pygame.K_LEFT]:\
            self.x1 -= 3\
            self.x2 -= 3\
\
        elif keys[pygame.K_RIGHT]:\
            self.x1 += 3\
            self.x2 += 3\
\
\
class Ball:\
    def __init__(self, speed):\
        self.surface = win\
        self.x = 290\
        self.y = 225\
        self.speed = speed\
        self.dx = random.choice([-1, 1])\
        self.dy = random.choice([-1, 1])\
\
    def draw_circle(self, radius):\
        pygame.draw.circle(self.surface, 'white', (self.x, self.y), radius)\
\
    def update(self):\
        self.x += self.speed * self.dx\
        self.y += self.speed * self.dy\
\
        if self.x > 450 or self.x < 0:\
            self.dx *= -1\
        if self.y > 450 or self.y < 0:\
            self.dy *= -1\
\
\
figure = Board(win)\
ball = Ball(1)\
while True:\
    for event in pygame.event.get():\
        if event.type == pygame.QUIT:\
            exit()\
\
    win.fill('black')\
    ball.draw_circle(7)\
    figure.move_by_keys()\
    figure.draw_line(10)\
    ball.update()\
\
    pygame.time.delay(5)\
    pygame.display.update()}