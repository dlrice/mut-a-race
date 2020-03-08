import pygame
from pygame.locals import (
    K_q,
    K_w,
    RLEACCEL,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)
from utils import load_json, get_animal_image

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
    def __init__(self, setup_file, track_size, n_levels):
        super(Player, self).__init__()
        setup = load_json(setup_file)
        self.images = setup['images']
        self.track_size = track_size
        body = self.images['body']
        surface = get_animal_image(**body)
        self.image = surface
        print(surface.get_size())
        # self.original_image = surface
        # factor = 0.1
        # width, height = surf.get_size()
        # scaled_size = (int(width*factor), int(height*factor))
        # self.surf = pygame.transform.smoothscale(surf, scaled_size)
        # self.surf.set_colorkey(None, RLEACCEL)
        self.rect = self.image.get_rect(center=body['center'])
        self.speed = 1
        self.min_speed = 1
        self.max_speed = 10
        # self.speak_sound = pygame.mixer.Sound('barking.ogg')
        # self.angle = 0
        self.level = 0
        self.n_levels = n_levels
        self.complete = False

    # def speak(self):
    #     self.speak_sound.play(maxtime=250)

    # def jiggle(self):
    #     # center = self.image.get_rect().center
    #     self.image = pygame.transform.rotate(self.original_image, self.angle)
    #     self.angle += 10
    #     # self.rect = self.image.get_rect(center=center)

    def finished_level(self):
        self.level += 1
        if self.level == self.n_levels:
            self.complete = True

    # Move the sprite based on user keypresses
    def update(self, pressed_keys):
        if (self.complete):
            return

        if pressed_keys[K_q]:
            self.speed = max(self.speed - 1, self.min_speed)
            # self.speak()
        elif pressed_keys[K_w]:
            self.speed = min(self.speed + 1, self.max_speed)
            # self.speak()
        self.rect.move_ip(self.speed, 0)

        # Detect completion of level
        if self.rect.right > self.track_size['width']:
            self.finished_level()
            print(self.level)
