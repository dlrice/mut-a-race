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
from pathlib import Path
from utils import get_background_image
from player import Player

pygame.init()

Path('./tmp').mkdir(exist_ok=True)
track_size = {'height': 200, 'width': 600}

screen_size = {'height': track_size['height']*3, 'width': track_size['width']}

background_image = get_background_image(
    'mountain_background', track_size['width'], track_size['height'])

screen = pygame.display.set_mode(
    (screen_size['width'], screen_size['height'])
)
pygame.display.set_caption('mut-race')

goat = Player('./goat.json', track_size)

all_sprites = pygame.sprite.Group([goat])

# Variable to keep the main loop running
running = True

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
    goat.update(pressed_keys)

    screen.blit(background_image, (0, 0))

    # Draw all sprites
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    pygame.display.flip()
