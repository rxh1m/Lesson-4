import pygame
pygame.init()

WIDTH = 1400
HEIGHT = 1200

screen = pygame.display.set_mode((WIDTH,HEIGHT))

rocket = pygame.image.load("Lesson 4/images/rocket.png")
rocket = pygame.transform.scale(rocket,(400,550))
background = pygame.image.load("Lesson 4/images/background.png")
background = pygame.transform.scale(background,(WIDTH,HEIGHT))


class Rocket(pygame.sprite.Sprite):
    def __init__(self,x,y,img):
        super().__init__()
        self.x = x
        self.y = y
        self.image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.image,(250,150))
        self.rect = self.image.get_rect()
        self.rect.center = x,y

rocket = Rocket(700,600,"Lesson 4/images/rocket.png")
rocket_group = pygame.sprite.Group()
rocket_group.add(rocket)
ufo = Rocket(700,300,"Lesson 4/images/ufo.png")
rocket_group.add(ufo)


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.QUIT()
    screen.fill("sky blue")
    screen.blit(background,(0,0))
    rocket_group.draw(screen)
    pygame.display.update()