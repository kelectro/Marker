#!/usr/bin/python

import cv2
import numpy as np;

im = cv2.imread('m1.jpg', cv2.IMREAD_GRAYSCALE)

# Simple blob detector
params = cv2.SimpleBlobDetector_Params()

# set threshold
params.minThreshold = 10
params.maxThreshold = 200

# Area filtering
params.filterByArea = True
params.minArea = 75
params.maxArea = 200

# no circularity needed
params.filterByCircularity = False
params.filterByConvexity = False
params.filterByInertia = False
# opencv version 4
# for older version <3
# use detector = cv2.SimpleBlobDetector(params)

detector = cv2.SimpleBlobDetector_create(params)

keypoints = detector.detect(im)

# Draw detected blobs as red circles.
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures
# the size of the circle corresponds to the size of blob

im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)


# Show blobs
cv2.imshow("Keypoints", im_with_keypoints)
cv2.waitKey(0)
