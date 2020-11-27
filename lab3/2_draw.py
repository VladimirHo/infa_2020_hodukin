import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

x1 = 100; y1 = 100
x2 = 300; y2 = 200
N = 10
color = (255, 255, 255)
hcolor = (128, 128, 128)
gcolor = (0, 255, 0)
rect(screen, hcolor, (x1, y1, x2 - x1, y2 - y1), 0)
h = (x2 - x1) // (N + 1)
x = x1 + h
for i in range(N):
    line(screen, gcolor, (x, y1), (x, y2))
    x += h

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()