import pygame
clock = pygame.time.Clock()
fps = 60

pygame.init()
width = 800
height = 600
screen = pygame.display.set_mode((width, height))

#RGB _ Red Green Blue
white = (255, 255, 255)
red = (255, 50, 50)
black = (0, 0, 0)
green = (50, 255, 50)
blue = (50, 50, 255)

marker_icon = pygame.image.load("images/marker.png")

pygame.display.set_caption("Paint")
pygame.display.set_icon(marker_icon)


class Marker:
    def __init__(self):
        self.size = 20
        self.rect = pygame.Rect(width/2, height/2, self.size, self.size)
        self.rect.center = [width/2, height/2]
        self.speed = 1
        self.speed_x = 0
        self.speed_y = 0
        self.color = black
        self.value = 5
        self.positioned = False

    def draw(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        pygame.draw.circle(screen, self.color, self.rect.center, self.size/2)
        self.rect = pygame.Rect(self.rect.x, self.rect.y, self.size, self.size)


marker = Marker()
screen.fill((255, 255, 255))


run = True
while run:
    clock.tick(fps)

    marker.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                marker.speed_y = marker.speed
            if event.key == pygame.K_UP:
                marker.speed_y = -marker.speed
            if event.key == pygame.K_LEFT:
                marker.speed_x = -marker.speed
            if event.key == pygame.K_RIGHT:
                marker.speed_x = marker.speed

            #ფერების ცვლილება
            if event.key == pygame.K_w:
                marker.color = white
            if event.key == pygame.K_d:
                marker.color = black
            if event.key == pygame.K_r:
                marker.color = red
            if event.key == pygame.K_g:
                marker.color = green
            if event.key == pygame.K_b:
                marker.color = blue

            #ზომები მარკერის
            if event.key == pygame.K_m:
                marker.size += marker.value
                marker.rect.centerx -= marker.value / 2
                marker.rect.centery -= marker.value / 2

            if event.key == pygame.K_n:
                marker.size -= marker.value
                marker.rect.x += marker.value / 2
                marker.rect.y += marker.value / 2


        if event.type == pygame.KEYUP:
            if event.key in [pygame.K_DOWN, pygame.K_UP]:
                marker.speed_y = 0
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                marker.speed_x = 0


        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if marker.rect.collidepoint(event.pos):
                    marker.positioned = True
                else:
                    marker.rect.center = event.pos


        if event.type == pygame.MOUSEBUTTONUP:
            marker.positioned = False

        if event.type == pygame.MOUSEMOTION and marker.positioned == True:
            marker.rect.move_ip(event.rel)

    pygame.display.update()
