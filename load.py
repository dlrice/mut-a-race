#!/usr/bin/env python3
import pygame
from PIL import Image
from utils import get_resource_path

background_image_path = get_resource_path('grass')
background_image_object = Image.open(background_image_path)

# Create the screen object
screen = pygame.display.set_mode(
    background_image_object.size
)

background_image = pygame.image.load(background_image_object).convert()


# Main loop
while running:
    # Look at every event in the queue
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            # Was it the Escape key? If so, stop the loop.
            if event.key == K_ESCAPE:
                running = False

        # Did the user click the window close button? If so, stop the loop.
        elif event.type == QUIT:
            running = False

    # Get the set of keys pressed and check for user input
    pressed_keys = pygame.key.get_pressed()

    # screen.fill((135, 206, 250))
    screen.blit(background_image, (0, 0))
