import pygame
import sys
from random import randint

pygame.init()

screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("My Pygame")

rect_color = pygame.Color('lightyellow')
fill_color = (32, 52, 71)

rect_width, rect_height = 100, 200
x = (screen_width - rect_width)/2
y = (screen_height - rect_height)/2
step = 25

while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and y >= step:
                y -= step
                print(y)
            if event.key == pygame.K_DOWN and y <= screen_height - rect_height - step:
                y += step
            if event.key == pygame.K_LEFT and x >= step:
                x -= step
                print(x)
            if event.key == pygame.K_RIGHT and x <= screen_width - rect_width - step:
                x += step


    screen.fill(fill_color)
    pygame.draw.rect(screen, rect_color, (x, y, rect_width, rect_height))
    pygame.display.update()

