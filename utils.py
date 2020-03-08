#!/usr/bin/env python3
import json
from PIL import Image, ImageChops
import pygame.image
import os.path


def load_json(path):
    with open(path) as f:
        return json.load(f)


def get_resource_paths():
    return load_json('./resource_paths.json')


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
    return pygame.image.frombuffer(image.tobytes(), image.size, image.mode).convert_alpha()


def resize_height_crop_width(in_path, out_path, resize_height, crop_width, x_offset):
    image = Image.open(in_path)
    width, height = image.size
    ratio = resize_height / height
    scaled_width = int(width * ratio)
    image = image.resize((scaled_width, resize_height), Image.ANTIALIAS)
    image = image.crop((x_offset, 0, x_offset + crop_width, resize_height))
    file_root, file_ext = os.path.splitext(in_path)
    image.save(out_path)


def trim_image(image):
    bg = Image.new(image.mode, image.size, image.getpixel((0, 0)))
    diff = ImageChops.difference(image, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    if bbox:
        return image.crop(bbox)


def get_animal_image(path, width, **kwargs):
    image = trim_image(Image.open(path))
    image = trim_image(image)
    image_width, image_height = image.size
    ratio = image_height / image_width
    scaled_height = int(ratio * width)
    image = image.resize((width, scaled_height), Image.ANTIALIAS)
    return pygame.image.frombuffer(image.tobytes(), image.size, image.mode).convert_alpha()
