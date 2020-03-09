#!/usr/bin/env python3

import pygame

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
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
from utils import get_background_image
from player import Player

pygame.init()

track_size = {'height': 200, 'width': 1000}


screen_size = {'height': track_size['height']*3, 'width': track_size['width']}
screen = pygame.display.set_mode(
    (screen_size['width'], screen_size['height']),
    pygame.HWSURFACE  # pygame.FULLSCREEN,
)

levels = ['mountain_background']

pygame.display.set_caption('mut-a-race')

goat = Player('./goat.json', track_size, levels, 0)
horse = Player('./horse.json', track_size, levels, 1)
rabbit = Player('./rabbit.json', track_size, levels, 2)

# all_sprites = pygame.sprite.Group([goat])

# Variable to keep the main loop running
running = True

# Setup the clock for a decent framerate
clock = pygame.time.Clock()
FPS = 30

# Main loop
while running:
    # Look at every event in the queue
    for event in pygame.event.get():
        # Did the user hit a key?
        if event.type == KEYDOWN:
            # Was it the Escape key? If so, stop the loop.
            if event.key == K_ESCAPE:
                running = False

        # Did the user click the window close button? If so, stop the loop.
        elif event.type == QUIT:
            running = False

    # Get the set of keys pressed and check for user input
    pressed_keys = pygame.key.get_pressed()
    goat.update(pressed_keys, screen)
    horse.update(pressed_keys, screen)
    rabbit.update(pressed_keys, screen)

    # # Draw all sprites
    # for entity in all_sprites:
    #     screen.blit(entity.image, entity.rect)

    pygame.display.flip()

    # Ensure program maintains a rate of 30 frames per second
    clock.tick(FPS)
