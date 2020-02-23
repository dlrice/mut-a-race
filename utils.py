#!/usr/bin/env python3
import json
from PIL import Image
import pygame.image


def get_resource_paths():
    with open('./resource_paths.json') as f:
        return json.load(f)


resource_paths = get_resource_paths()


def get_resource_path(resource):
    return resource_paths[resource]


def get_background_image(name, crop_width, resize_height, x_offset=0):
    path = get_resource_path(name)
    width, height = Image.open(path).size
    ratio = resize_height / height
    scaled_width = int(width * ratio)
    image = Image.open(path)
    image = image.resize((scaled_width, resize_height), Image.ANTIALIAS)
    image = image.crop((x_offset, 0, x_offset + crop_width, resize_height))
    print(image.size, image.mode)
    return pygame.image.fromstring(image.tobytes(), image.size, image.mode)
