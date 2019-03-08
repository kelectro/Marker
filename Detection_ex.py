import cv2
import numpy as np

orig = cv2.imread('/home/thanasis/Documents/eagles/Markers-eagles -20190213T183437Z-001/Markers-eagles /IMG_20190213_115706.jpg')
gray = cv2.cvtColor(orig, cv2.COLOR_BGR2GRAY)
cv2.namedWindow('original', cv2.WINDOW_NORMAL)

cv2.imshow('original', gray)

cv2.waitKey(0)
cv2.destroyAllWindows()
