import pygame
from pygame import *
import sys
from math import *


pygame.init()

width = 400
height = 400
screen = display.set_mode((width, height))
display.set_caption("RUUT")

värv = (35, 118, 69)

ekraanikeskpunktx = width / 2
ekraanikeskpunkty = height / 2
küljepikkus = 100
nurk = 60

vertexid = []

küljed = 0

while (küljed < 6):
    seenurk = nurk + küljed *60
    nurgaradiaan = radians(seenurk)
    x = ekraanikeskpunktx +cos(nurgaradiaan) * küljepikkus
    y = ekraanikeskpunkty +sin(nurgaradiaan) * küljepikkus
    vertexid.append((x,y))
    küljed +=1

mängJookseb = True
while mängJookseb:
    screen.fill((255,255,255))
    draw.polygon(screen, värv, vertexid)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mängJookseb = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mängJookseb = False