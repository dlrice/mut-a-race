#!/usr/bin/env python3
from PIL import Image
import os.path
from utils import get_resource_path

in_path = get_resource_path('grass')
resize_height = 400
crop_width = 800
x_offset = 800

image = Image.open(in_path)
width, height = image.size
ratio = resize_height / height
scaled_width = int(width * ratio)
image = image.resize((scaled_width, resize_height), Image.ANTIALIAS)
image = image.crop((x_offset, 0, x_offset + crop_width, resize_height))
file_root, file_ext = os.path.splitext(in_path)
# out_path = f'{file_root}.{crop_width}x{resize_height}{file_ext}'
out_path = 'temp.png'
image.save(out_path)
