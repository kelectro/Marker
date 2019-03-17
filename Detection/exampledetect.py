#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  exampledetect.py
#  
#  Copyright 2019 thanasis <thanasis@thanasis>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import cv2
import numpy as np
import matplotlib.pyplot as plt
import  glob
import  sys

orig = cv2.imread('/home/thanasis/Documents/eagles/Markers-eagles -20190213T183437Z-001/resized/resized_52.jpg')
#templ = cv2.imread('/home/thanasis/Documents/eagles/Markers-eagles -20190213T183437Z-001/Markers-eagles /IMG_20190213_115706(crop).jpg', 0)
medBlur = cv2.medianBlur(orig, 9)
gray = cv2.cvtColor(medBlur, cv2.COLOR_BGR2GRAY)


#corner detection
corners = cv2.goodFeaturesToTrack(gray, 200, 0.01, 4)
corners = np.int0(corners)
for corner in corners:
    x, y = corner.ravel()
    cv2.circle(orig, (x, y), 3, 255, -1)

edges = cv2.Canny(orig, 500, 300)



cv2.imshow('original', orig)
cv2.imshow('corner', orig)


cv2.imshow('edges', edges)


cv2.waitKey(0)
cv2.destroyAllWindows()
