#!/bin/python
import os
import sys
resolution, grid = sys.argv[1:]
resolution_x, resolution_y = [int(i) for i in resolution.split('x')]
grid_x, grid_y = [int(i) for i in grid.split('x')]
total_x = resolution_x * grid_x
total_y = resolution_y * grid_y

if not os.path.exists('./BlackMarble_2016_3km_geo.tif'):
    print('Downloading Nasa Earth Night...')
    os.system('wget https://eoimages.gsfc.nasa.gov/images/imagerecords/144000/144898/BlackMarble_2016_3km_geo.tif')
if not os.path.exists('resized.png'):
    print('Resizing image...')
    os.system(f'convert ./BlackMarble_2016_3km_geo.tif -resize {total_x}x{total_y}^ -gravity northwest resized.png')
if not os.path.exists('croped'):
    print('Cropping image...')
    os.mkdir('cropped')
    for gx in range(grid_x):
        for gy in range(grid_y):
            os.system(f'convert ./resized.png -crop {resolution_x}x{resolution_y}+{resolution_x*gx}+{resolution_y*gy} cropped/{gy}x{gx}.png')
