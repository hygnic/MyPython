import pygame
import sys


height = 1200
width = 800
screen = pygame.display.set_mode((height, width))
screen.fill((200, 230, 200))
while True:
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            print(event.key)
