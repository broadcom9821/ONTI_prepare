# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cv2
import os 
import glob
path = "/Users/vladimirbessonov/Documents/ONTI_prepare/tlr_offline/traffic_light_images/training"
colors = ["red", "green", "yellow"]
for color in colors:
    path = os.path.join(path, color)
    os.path.join(path, "*.jpg")
    alf = glob.glob(os.path.join(path, "*.jpg"))
    for fl in alf:
        print(fl)