import pygame
import sys
from random import randint
from pygame import  mixer
#ფაიგეიმის ინიციაცია
pygame.init()

mixer.init()
mixer.music.load("static/background.mp3")
mixer.music.play(-1)
mixer.music.set_volume(0.5)

# სიხშირის კონტროლი
clock = pygame.time.Clock()
fps = 30

#ეკრანის ზომები
width = 1366
height = 768
#ეკრანის შექმნა
screen = pygame.display.set_mode((width, height))

#საჭირო მასალების შემოტანა
background = pygame.image.load("static/background.png")
animation1 = pygame.image.load("static/animation1.png")
animation2 = pygame.image.load("static/animation2.png")
snowflake = pygame.image.load("static/snowflake.png")
snowflake = pygame.transform.scale(snowflake, (50, 50))

#RGB _ red green blue
red = (255, 50, 50)
yellow = (255, 255, 50)

font = pygame.font.Font("static/font.ttf", 120)

tree_images = [animation1, animation2]


#ეკრანის აიქონი და წარწერა
pygame.display.set_icon(animation1)
pygame.display.set_caption("Christmas Card")

#ფიფქების კლასი
class SnowFlake(pygame.sprite.Sprite):
    def __init__(self, image, h, v):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = [randint(-1000, width + 1000), randint(-500, -25)]
        self.speed_h = h
        self.speed_v = v

    def update(self):
        self.rect.y += self.speed_v
        self.rect.x += self.speed_h

        if self.rect.y > height or self.rect.y < -1000:
            self.kill()



#ნაძვის ხის კლასი
class ChristmasAnimation:
    def __init__(self, images_list, loc_x, loc_y):
        self.images = images_list
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.center = [loc_x, loc_y]
        self.i = 0

    def draw(self):
        global counter
        screen.blit(self.image, self.rect)

        if counter == 0:
            if self.i < len(self.images) - 1:
                self.i += 1
            else:
                self.i = 0
            self.image = self.images[self.i]





tree = ChristmasAnimation(tree_images, 200, 500)

#მთვლელი
counter = 0

def create_snow(mn, mx):
    if counter == 0:
        for _ in range(randint(mn, mx)):
            flake = SnowFlake(snowflake, 15, 30)
            snow_group.add(flake)

    snow_group.draw(screen)
    snow_group.update()


snow_group = pygame.sprite.Group()


color = red
#მილოცვა
def message(color, font):
    rendered_text = font.render("Happy New Year 2024!", False, color)
    text_rect = rendered_text.get_rect()
    text_rect.center = [width/2, height//6]
    screen.blit(rendered_text, text_rect)



#მთავარი ციკლის გამომრთველი
run = True
#მთავარი ციკლი
while run:
    clock.tick(fps)
    counter += 1
    if counter > 15:
        counter = 0
        if color == red:
            color = yellow
        else:
            color = red



    screen.blit(background, (0, 0))
    tree.draw()
    message(color, font)
    create_snow(20, 40)
    #მისალოცი ბარათის გათიშვის კოდი
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
sys.exit()