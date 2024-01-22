import pygame

pygame.init()

laptop_info = pygame.display.Info()

width = laptop_info.current_w
height = laptop_info.current_h

screen = pygame.display.set_mode((width, height))

run = True

while run:
    for event in pygame.event.get():
        # if event.type == pygame.QUIT:
        #     run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
