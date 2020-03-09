import pygame
from utils import get_animal_image


class BodyPart(pygame.sprite.Sprite):
    def __init__(self, config, y):
        super(BodyPart, self).__init__()
        surface = get_animal_image(**config)
        self.image = surface
        center = config['center']
        self.rect = self.image.get_rect(center=(center[0], center[1] + y))

    def update(self, delta):
        self.rect.move_ip(delta, 0)
