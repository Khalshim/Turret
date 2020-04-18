from constante import *
from math import *
from random import randint
class Laser(pygame.sprite.Sprite):

    def __init__(self, player, x,y ):
        super().__init__()

        self.image = laserIMG
        self.origin_image = self.image
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.xChange = 0
        self.yChange = 0
        self.speed = 5

        self.angle = player.angle
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        old_center = self.rect.center
        self.rect = self.image.get_rect(center=old_center)

        self.distance = int(
            sqrt((self.rect.x - self.rect.x + self.rect[2])**2 + (self.rect.y - self.rect.y + self.rect[3])**2))



    def move(self):
        self.xChange = cos(degrees(self.angle)) * self.speed
        self.yChange = sin(degrees(self.angle)) * self.speed

        self.rect.x = self.rect.x + self.xChange
        self.rect.y = self.rect.y + self.yChange
