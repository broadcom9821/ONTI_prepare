#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 23:33:53 2020

@author: vladimirbessonov
"""


import cv2 

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
cam = cv2.VideoCapture("/Users/vladimirbessonov/Downloads/output5.mkv")

while(True):
    ret, frame = cam.read()
    frame = cv2.resize(frame, (400,300))
    (rects, weights) = hog.detectMultiScale(frame, scale = 1.1, winStride = (2,2))
    
    for (x,y,w,h) in rects:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0),2)
    
    cv2.imshow("winname", frame)
    
    if cv2.waitKey(1)==ord("q"):
        break
    
cv2.destroyAllWindows()
cam.release()