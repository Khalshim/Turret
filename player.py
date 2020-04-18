from constante import *
import math
from laser import Laser
class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = playerIMG
        self.rect = self.image.get_rect()
        self.rect.x = ecranW/2
        self.rect.y = ecranH/2
        self.angle = 0
        self.origin_image = self.image
        self.lasers = pygame.sprite.Group()

    def shoot(self):
        self.lasers.add(Laser(self, self.rect.centerx, self.rect.centery))


    def rotating(self):
        mouse = pygame.mouse.get_pos()
        print(self.angle)
        offset = (self.rect.centerx - mouse[0], self.rect.centery - mouse[1])
        self.angle = math.degrees(math.atan2(*offset))
        old_center = self.rect.center
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=old_center)

        self.distance = int(math.sqrt((offset[0] * offset[0]) + (offset[1] * offset[1])))
