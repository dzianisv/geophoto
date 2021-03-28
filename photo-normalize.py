#!/usr/bin/env python3
import sys
import os
from PIL import Image

TARGET_RESOLUTION = (3840, 2160)
TARGET_RATIO = TARGET_RESOLUTION[0]/TARGET_RESOLUTION[1]


class SmallImage(Exception):
    pass

def normalize(file_path):
    # Opens a image in RGB mode 
    im = Image.open(file_path) 
    
    width, height = im.size 
    
    if width < TARGET_RESOLUTION[0]:
        raise SmallImage()
    if height < TARGET_RESOLUTION[1]:
        raise SmallImage() 
    
    ratio = width/height
    
    portrait = width > height
    if portrait:
        new_size = (TARGET_RESOLUTION[0], int(width/ratio))
    else:
        new_size = (int(height * ratio), TARGET_RESOLUTION[1])
    
    im = im.resize(new_size)
    
    if portrait:
        y = (new_size[1] - TARGET_RESOLUTION[1])/2
        crop_points = (0, y, TARGET_RESOLUTION[0], y+TARGET_RESOLUTION[1])  
    else:
        x = (new_size[0] - TARGET_RESOLUTION[0])/2
        crop_points = (x, 0, x+TARGET_RESOLUTION[0], TARGET_RESOLUTION[1])
    
    im = im.crop(crop_points)
    
    new_path = os.path.join("normalized", os.path.basename(file_path))
    
    if not os.path.exists("normalized"):
        os.mkdir("normalized")
    
    im.save(new_path)
    
    mtime = os.path.getmtime(file_path)
    os.utime(new_path, (mtime, mtime))
    

for file_path in sys.argv[1:]:
    normalize(file_path)
