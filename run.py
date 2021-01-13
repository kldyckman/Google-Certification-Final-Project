#!/usr/bin/env python3
import os, sys
import json
import requests

path = "supplier-data/descriptions/"
url = "http://localhost/fruits/"
descriptions = os.listdir(path)

for description in descriptions:
  if description.endswith("txt"):
    with open(path + description, 'r') as item:
      fruit_name = os.path.splitext(description)[0]
      data = item.read().split("\n")
      fruit_dict = {"name":data[0], "weight":int(data[1].strip(" lbs")), "description":data[2], "image_name": fruit_name + ".jpeg"}
      response = requests.post(url, json=fruit_dict)
      response.raise_for_status()
      print(response.request.url)
      print(response.status_code)