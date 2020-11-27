import pygame
from pygame.draw import *
from math import radians, sin, cos

def rot(x, y, s, c):
    return (x * c + y * s, y * c - x * s)

def rrect(screen, x, y, w, h, fg):
    fr = radians(fg)
    c = cos(fr)
    s = sin(fr)
    x1, y1 = w / 2, h / 2
    ps = [rot(x1, y1, s, c), rot(x1, -y1, s, c),
              rot(-x1, -y1, s, c), rot(-x1, y1, s, c)]
    ps1 = [(p[0] + x, p[1] + y) for p in ps]
    print(ps1)
    polygon(screen, (0, 0, 0), ps1)

pygame.init()

FPS=30
w=400; h=400;
screen=pygame.display.set_mode((w, h))

x1 = 100
y1 = 100
x2=300; y2=200
x3=200
y3=300
center=(w // 2, h // 2)
h=(45, 20)
bx=(50, 8)
c1=(center[0] - h[0], center[1] - h[1])
c2=(center[0] + h[0], center[1] - h[1])
r=100
r10=8
r11=20
r20=8
r21 = 15
color=(255, 255, 255)
blcolor=(0, 0, 0)
hcolor=(128, 128, 128)
rcolor=(255, 0, 0)
gcolor=(0, 255, 0)
bcolor=(255, 0, 0)
ycolor=(255, 255, 0)
rect(screen, hcolor, (0, 0, 400, 400))
circle(screen, ycolor, center, r)
circle(screen, blcolor, center, r, 2)
circle(screen, rcolor, c1, r11)
circle(screen, blcolor, c1, r11, 1)
circle(screen, blcolor, c1, r10)
circle(screen, rcolor, c2, r21)
circle(screen, blcolor, c2, r21, 1)
circle(screen, blcolor, c2, r20)
rrect(screen, 200, 260, 90, 15, 0)
rrect(screen, 140, 150, 100, 8, -20)
rrect(screen, 260, 150, 100, 8, 30)
pygame.display.update()
clock=pygame.time.Clock()
finished=False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()