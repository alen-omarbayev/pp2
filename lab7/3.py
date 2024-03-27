import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Red Circle")

WHITE = (255, 255, 255)
RED = (255, 0, 0)

ball_radius = 25
ball_x = 400
ball_y = 300
ball_speed = 20

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        ball_y = max(ball_y - ball_speed, ball_radius)
    if keys[pygame.K_DOWN]:
        ball_y = min(ball_y + ball_speed, 600 - ball_radius)
    if keys[pygame.K_LEFT]:
        ball_x = max(ball_x - ball_speed, ball_radius)
    if keys[pygame.K_RIGHT]:
        ball_x = min(ball_x + ball_speed, 800 - ball_radius)

    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)
    pygame.display.flip()
    clock.tick(30)
