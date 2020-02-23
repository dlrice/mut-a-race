#!/usr/bin/env python3
import pygame
from pygame.locals import *
from PIL import Image
from utils import get_resource_path

def get_background_image(name, width, height):
    path = get_resource_path(name)
    width, height = Image.open(path).size
    ratio = resize_height / height
    scaled_width = int(width * ratio)
    image = Image.open(in_path)
    image = image.resize((scaled_width, resize_height), Image.ANTIALIAS)
    image = image.crop((x_offset, 0, x_offset + crop_width, resize_height))
    return pygame.image.fromstring(image.tobytes(), image.size, image.mode)
    
# Create the screen object
screen = pygame.display.set_mode()

running = True

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
