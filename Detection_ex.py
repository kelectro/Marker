import cv2
import numpy as np
from matplotlib import pyplot as plt

#orig = cv2.imread('/home/thanasis/Documents/eagles/Markers-eagles -20190213T183437Z-001/Markers-eagles /IMG_20190213_115706.jpg')
orig = cv2.imread('/home/thanasis/Documents/eagles/Markers-eagles -20190213T183437Z-001/Markers-eagles /IMG_20190213_115601.jpg')
gray = cv2.cvtColor(orig, cv2.COLOR_BGR2GRAY)

# Initiate ORB detector
orb = cv2.ORB_create()
# find the keypoints with ORB
kp = orb.detect(gray, None)
# compute the descriptors with ORB
kp, des = orb.compute(gray, kp)
# draw only keypoints location,not size and orientation
img2 = cv2.drawKeypoints(gray, kp, gray, color=(0, 255, 0), flags=0)

plt.imshow(img2), plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
