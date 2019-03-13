import cv2
import numpy as np
import matplotlib.pyplot as plt

orig = cv2.imread('/home/thanasis/Documents/eagles/Markers-eagles -20190213T183437Z-001/Markers-eagles /IMG_20190213_115706.jpg', 0)
templ = cv2.imread('/home/thanasis/Documents/eagles/Markers-eagles -20190213T183437Z-001/Markers-eagles /IMG_20190213_115706(crop).jpg', 0)
#gray = cv2.cvtColor(orig, cv2.COLOR_BGR2GRAY)
#gray = np.float32(gray)
'''
corners = cv2.goodFeaturesToTrack(gray, 1000, 0.1, 4)
corners = np.int0(corners)
for corner in corners:
    x, y = corner.ravel()
    cv2.circle(orig, (x, y), 3, 255, -1)
'''

orb = cv2.ORB_create()

kp1, des1 = orb.detectAndCompute(templ, None)
kp2, des2 = orb.detectAndCompute(orig, None)

bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

matches = bf.match(des1, des2)
matches = sorted(matches, key=lambda x:x.distance)

img3 = cv2.drawMatches(templ, kp1, orig, kp2, matches[:20], None, flags=2)
plt.imshow(img3)
plt.show()
#edges = cv2.Canny(gray, 500, 350)



cv2.imshow('original', orig)
#cv2.imshow('corner', orig)


#cv2.imshow('laplacian', laplacian)
#cv2.imshow('edges', edges)


cv2.waitKey(0)
cv2.destroyAllWindows()
