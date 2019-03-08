#!/usr/bin/python
#load packages

import argparse
import cv2
import imutils as imutils
import numpy as np


img=cv2.imread("m1.jpg")

#convert to gray , blur, find edges
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blurred =cv2.GaussianBlur(gray,(7,7),0)
edges=cv2.Canny(blurred,10,300)

#contours
cont=cv2.findContours(edges.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cont=imutils.grab_contours(cont)

for c in cont :
    area=cv2.contourArea(c)
    perimeter=cv2.arcLength(c,True)
    approx= cv2.approxPolyDP(c,0.01*perimeter,True)
    print(len(approx))
    #is it rectangular?
    if len(approx) >=4 and len(approx)<=10:
        (x, y, w, h)=cv2.boundingRect(approx)
        aspectRatio=w/float(h)
        hullArea=cv2.contourArea(cv2.convexHull(c))
        print("skata",hullArea)
        solidity = area / float(hullArea)

    # compute whether or not the width and height, solidity, and
    # aspect ratio of the contour falls within appropriate bounds
        keepDims = w > 25 and h > 25
        keepSolidity = solidity > 0.9
        keepAspectRatio = aspectRatio >= 0.8 and aspectRatio <= 1.2

    # ensure that the contour passes all our tests
        print(keepDims, keepSolidity,keepAspectRatio)
        if keepDims and keepSolidity and keepAspectRatio:

        #draw outline

            cv2.drawContours(img, [approx], -1, (0, 0, 255), 4)
            status = "Target(s) Acquired"

        # compute the center of the contour region and draw the
        # crosshairs
            M = cv2.moments(approx)
            (cX, cY) = (int(M["m10"] // M["m00"]), int(M["m01"] // M["m00"]))
            (startX, endX) = (int(cX - (w * 0.15)), int(cX + (w * 0.15)))
            (startY, endY) = (int(cY - (h * 0.15)), int(cY + (h * 0.15)))
            cv2.line(img, (startX, cY), (endX, cY), (0, 0, 255), 3)
            cv2.line(img, (cX, startY), (cX, endY), (0, 0, 255), 3)
        # draw the status text on the frame
        cv2.putText(img, status, (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(0, 0, 255), 2)

        # show the frame and record if a key is pressed
        cv2.imshow("Frame", img)
        key = cv2.waitKey()

        # if the 'q' key is pressed, stop the loop
        if key == ord("q"):
            break

    # cleanup the camera and close any open windows
    #camera.release()
    cv2.destroyAllWindows()

