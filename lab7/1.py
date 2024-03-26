import pygame 
import time
import datetime
import math

pygame.init()
RES = WIDTH ,HEIGHT = 1400,1050
middle = WIDTH//2 , HEIGHT//2
RADIUS = 1000

screen = pygame.display.set_mode((RES))
clock = pygame.time.Clock()

pygame.display.set_caption("Mickey Clock")

sec = pygame.image.load(r"C:\Users\ASUS\OneDrive\Рабочий стол\pp2\pp2\lab7\leftarm.png").convert_alpha()
minute = pygame.image.load(r"C:\Users\ASUS\OneDrive\Рабочий стол\pp2\pp2\lab7\rightarm.png").convert_alpha()
rectsec = sec.get_rect()
rectmin = minute.get_rect()
rectmin.center = middle
rectsec.center = middle
background = pygame.image.load(r"C:\Users\ASUS\OneDrive\Рабочий стол\pp2\pp2\lab7\mainclock.png")
run = True

angle1 = 0
angle2 = 0
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    #system time
    time = datetime.datetime.now()
    minuteTime = time.minute
    secondTime = time.second

    #minute
    angle1 = -minuteTime*6 
    leg1 = pygame.transform.rotate(minute, angle1)
    rect1 = leg1.get_rect()
    rect1.center = rectmin.center

    #second
    angle2 = -secondTime*6 
    leg2 = pygame.transform.rotate(sec, angle2)
    rect2 = leg2.get_rect()
    rect2.center = rectsec.center
    
    #output
    screen.blit(background, (0, 0))
    screen.blit(leg1, rect1)
    screen.blit(leg2, rect2)

    pygame.display.flip()
    clock.tick(60)