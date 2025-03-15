#!/usr/bin/env python3

# This script takes a sprite sheet file as an argument and outputs a sprite
# sheet with 1 pixel of padding between all the sprites.
#
# Example:
# `python add_padding.py input.png output.png`

import sys
from PIL import Image

def pad_sprite(sprite: Image):
    new_width = sprite.width + 2
    new_height = sprite.height + 2

    # Create sprite with a 1 pixel border
    new_sprite = Image.new("RGBA", (new_width, new_height), (0, 0, 0, 0))

    new_sprite.alpha_composite(sprite, (0, 0))
    new_sprite.alpha_composite(sprite, (2, 2))
    new_sprite.alpha_composite(sprite, (2, 0))
    new_sprite.alpha_composite(sprite, (0, 2))
    new_sprite.alpha_composite(sprite, (1, 0))
    new_sprite.alpha_composite(sprite, (0, 1))
    new_sprite.alpha_composite(sprite, (1, 2))
    new_sprite.alpha_composite(sprite, (2, 1))
    new_sprite.alpha_composite(sprite, (1, 1))

    return new_sprite

def pad_sprite_sheet(sprite: Image, columns: int, rows: int, tile_size: int):
    new_width = sprite.width + (columns * 2)
    new_height = sprite.height + (rows * 2)

    new_sprite = Image.new("RGBA", (new_width, new_height), (0, 0, 0, 0))

    for column in range(columns):
        for row in range(rows):
            # Extract a tile from the original sprite sheet
            pixel_x = column * tile_size
            pixel_y = row * tile_size
            croped = file.crop((pixel_x, pixel_y, pixel_x + tile_size, pixel_y + tile_size))

            paded_sprite = pad_sprite(croped)

            # Add the sprite to the new sprite sheet
            new_pixel_x = column * paded_sprite.width
            new_pixel_y = row * paded_sprite.height
            new_sprite.alpha_composite(paded_sprite, (new_pixel_x, new_pixel_y))

    return new_sprite

# Check arguments
if len(sys.argv) != 3:
    print("Must pass exactly 2 argument. An input path and an output path")
    exit(1)

input_path = sys.argv[1]
output_path = sys.argv[2]

file = Image.open(input_path, mode='r')

paded_sprite = pad_sprite_sheet(file, 12, 8, 4)
paded_sprite.save(output_path)
