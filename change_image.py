#!/usr/bin/env python3
import os, sys
from PIL import Image

path = "supplier-data/images/"
images = os.listdir(path)

for image in images:
  if "tiff" in image:
    file_name = os.path.splitext(image)[0]
    outfile = "supplier-data/images/" + file_name + ".jpeg"
    try:
      Image.open(path + image).convert('RGB').resize((600,400)).save(outfile,"JPEG")
    except IOError:
      print("cannot convert", image)