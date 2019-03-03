#!/usr/bin/python
#load packages

import argparse
import cv2
import imutils as imutils
import numpy as np

img=[cv2.imread]
img=cv2.imread("Marker1.jpg")

#convert to gray , blur, find edges
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blurred =cv2.GaussianBlur(gray,(7,7),0)
edges=cv2.Canny(blurred,50,150)

#contours
cont=cv2.findContours(edges.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cont=imutils.grab_contours(cont)

for c in cont :
    ares=cv2.contourArea(c)
    perimeter=cv2.arcLength(c,True)
    approx= cv2.approxPolyDP(c,0.01*perimeter,True)

    #is it rectangular?
    if len(approx) >=4 and len(approx)<=6 :
        (x, y, w, h)=cv2.boundingRect(approx)
        aspectRatio=w/float(h)

    hullArea=cv2.contourArea(cv2.convexHull(c))







'''
cv2.imwrite('houghlines3.jpg',img)
cv2.imshow('image',img)
'''



cv2.waitKey(0)
cv2.destroyAllWindows()