import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

x1 = 100; y1 = 100
x2 = 300; y2 = 200
x3 = 200; y3 = 300
r = 50
N = 10
color = (255, 255, 255)
hcolor = (128, 128, 128)
gcolor = (0, 255, 0)
rcolor = (255, 0, 0)
polygon(screen, hcolor, [[x1, y1], [x1, y2],
        [x3, y3], [x2, y2], [x2, y1]], 0)
h = (x2 - x1) // (N + 1)
x = x1 + h
for i in range(N):
    line(screen, gcolor, (x, y1), (x, y2))
    x += h
circle(screen, rcolor, (x3, y3), r, 2)
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()