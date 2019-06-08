# WORK IN PROGRESS
#TODO: add functions
import pygame_sdl2
pygame_sdl2.import_as_pygame()
import sys
import pygame
from pygame.locals import *
import random as rand
import time

pygame.init()
clock = pygame.time.Clock()
infoObject = pygame.display.Info() # get display resolution
width = infoObject.current_w
height = infoObject.current_h
surface = pygame.display.set_mode((width, height)) # setting display size
rect = pygame.Rect((0, 0), (128, 128))
surfrect = surface.get_rect()
rect.center = (surfrect.w / 2, surfrect.h / 2)

FPS = 60
size = 128
x = width // 2 - size // 2
y = height // 2 - size // 2
touched = False
in_motion = False
RECT_COLOR = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
myFont = pygame.font.SysFont("david", 64)
start = False
start_time = 0
end_time = 0

miss = 0
score = 0
while True:
    while int(end_time-start_time) >= 60:
        surface.blit(scoreLabel, (10, 10))
        surface.blit(timeLabel, (width//2-len(str(int(end_time-start_time)))*36, 10))
        surface.blit(missLabel, (width - (len('Missed: ' + str(miss)) * 36), 10))
        pygame.display.flip()
    
    while not start:
        startButton = pygame.Rect((0, 0), (width, height))
        startRect = pygame.Rect((x, y), (size, size))
        startLabel = myFont.render('Click on the screen to start', 1, WHITE)
        surface.fill(BLACK)
        surface.fill(BLACK, startButton)
        surface.fill(RECT_COLOR, startRect)
        surface.blit(startLabel, (x//4, y//2))
        pygame.display.flip()
        for ev in pygame.event.get():
            if ev.type == QUIT:
                pygame.quit()
            elif ev.type == pygame.MOUSEBUTTONDOWN:
                if startButton.collidepoint(ev.pos):
                    start_time = time.time()
                    score = 0
                    miss = 0
                    start = True
    rect = pygame.Rect((x, y), (size, size))
    for ev in pygame.event.get():
        if ev.type == QUIT:
            pygame.quit()
        elif ev.type == pygame.MOUSEBUTTONDOWN:
            if rect.collidepoint(ev.pos):
                touched = True
            else:
            	miss += 1
        elif ev.type == pygame.MOUSEBUTTONUP:
            touched = False
    surface.fill(BLACK)
    if touched:
        y = rand.randint(50, height-size) # from 50 becuase the score line
        x = rand.randint(0, width-size)
        score += 1
        touched = False
    else:
        pass
    end_time = time.time()
    scoreLabel = myFont.render('Score: ' + str(score), 1, WHITE)
    missLabel = myFont.render('Missed: ' + str(miss), 1, WHITE)
    timeLabel = myFont.render(str(int(end_time-start_time)), 1, WHITE)
    surface.blit(scoreLabel, (10, 10))
    surface.blit(timeLabel, (width//2-len(str(int(end_time-start_time)))*36, 10))
    surface.blit(missLabel, (width - (len('Missed: ' + str(miss)) * 36), 10))
    surface.fill(RECT_COLOR, rect)
    pygame.display.flip()
