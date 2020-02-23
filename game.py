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

pygame.init()

screen_size = {'height':  340, 'width': 600}


background_image = get_background_image(
    'grass_background', screen_size['width'], screen_size['height'])

screen = pygame.display.set_mode(
    (screen_size['width'], screen_size['height'])
)
pygame.display.set_caption('mut-race')

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

    screen.blit(background_image, (0, 0))
    pygame.display.flip()
