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


class Player(pygame.sprite.Sprite):
    def __init__(self, setup_file, track_size):
        super(Player, self).__init__()
        setup = load_json(setup_file)
        self.images = setup['images']
        self.track_size = track_size
        self.surf = pygame.image.load(self.images['body']).convert_alpha()
        # factor = 0.1
        # width, height = surf.get_size()
        # scaled_size = (int(width*factor), int(height*factor))
        # self.surf = pygame.transform.smoothscale(surf, scaled_size)
        # self.surf.set_colorkey(None, RLEACCEL)
        self.rect = self.surf.get_rect()
        self.speed = 10
        # self.speak_sound = pygame.mixer.Sound('barking.ogg')

    # def speak(self):
    #     self.speak_sound.play(maxtime=250)

    # Move the sprite based on user keypresses
    def update(self, pressed_keys):
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
