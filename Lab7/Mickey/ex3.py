import pygame
from datetime import datetime
import time

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Clock")

mick = pygame.transform.scale(pygame.image.load("clock.png"), (800, 600))
min = pygame.transform.scale(pygame.image.load("minute.png"), (800, 600))
sec = pygame.transform.scale(pygame.image.load("second.png"), (50, 600))

def rot_center(surf, image, angle, x, y):
    image = pygame.transform.rotate(image, angle)
    rect = image.get_rect(center=image.get_rect(center=(x, y)).center)
    surf.blit(image, rect)

    

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    screen.blit(mick, (0, 0))
    t = datetime.now()

    rot_center(screen, min, -t.minute * (6), 400, 300)
    rot_center(screen, sec, -t.second * (6), 400, 300)

    pygame.display.flip()
    clock.tick(30)
