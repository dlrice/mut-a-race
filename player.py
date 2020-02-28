import pygame
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)
from utils import load_json

jitters = [el - 10 for el in range(10)]


def rot_center(image, angle):
    """rotate an image while keeping its center and size"""
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image


class Player(pygame.sprite.Sprite):
    def __init__(self, setup_file, track_size):
        super(Player, self).__init__()
        setup = load_json(setup_file)
        self.images = setup['images']
        self.track_size = track_size
        surface = pygame.image.load(
            self.images['body']).convert_alpha()
        self.image = surface
        self.original_image = surface
        # factor = 0.1
        # width, height = surf.get_size()
        # scaled_size = (int(width*factor), int(height*factor))
        # self.surf = pygame.transform.smoothscale(surf, scaled_size)
        # self.surf.set_colorkey(None, RLEACCEL)
        self.rect = self.image.get_rect()
        self.speed = 10
        # self.speak_sound = pygame.mixer.Sound('barking.ogg')
        self.angle = 0

    # def speak(self):
    #     self.speak_sound.play(maxtime=250)

    def jiggle(self):
        # center = self.image.get_rect().center
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.angle += 10
        # self.rect = self.image.get_rect(center=center)

    # Move the sprite based on user keypresses
    def update(self, pressed_keys):
        self.jiggle()
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-self.speed, 0)
            # self.speak()
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(self.speed, 0)
            # self.speak()

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > self.track_size['width']:
            self.rect.right = self.track_size['width']
