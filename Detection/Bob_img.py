import cv2
import pytesseract
import numpy as np
#https://github.com/spmallick/learnopencv/blob/master/BlobDetector/blob.py
from PIL import Image
from matplotlib import pyplot as plt
import multiprocessing as mp
# g e a r g e...
# def f(x):
#     while 1:
#         pass  # infinite loop

# import multiprocessing as mp
# n_cores = mp.cpu_count()
# with mp.Pool(n_cores) as p:
#     p.map(f, range(n_cores))

def image_rot(img):
    rows,cols=img.shape
    i=0
    angle=0
    for angle in range (0,360,90):
        M=cv2.getRotationMatrix2D((cols/2,rows/2),angle,1)
        dst = cv2.warpAffine(img,M,(cols,rows))
        text=detect_test(dst)
        if (text == "G") :
            print("yoleleeee***************************************")
            exit()
        cv2.imshow("rot",dst)
        print("text",text)
        print("angle",angle)

    
def save_to_file(img):
    d+=1
    filename="/home/kiagkons/Documents/Eagles/Sdu_Eagles_Electronics/Detection/letters/im_%d.jpg"%d
    cv2.imwrite(filename,sharpened)
    print("done",d)

def detect_test(img):
    config = ('-l eng --oem 1 --psm 3')
    text = pytesseract.image_to_string(img, config=config)
    return text

   

frame=cv2.imread('g.jpg',0)
frame=cv2.resize(frame,(480,640))
cv2.imshow("Before",frame)
# Simple blob detector
params = cv2.SimpleBlobDetector_Params()

# set threshold
# #for 640*480 min 10 max 200
# params.minThreshold = 10
# params.maxThreshold = 200

# Area filtering
#640*480 75,250
params.filterByArea = True
params.minArea = 10
params.maxArea = 100

# Filter by Circularity
params.filterByCircularity = True
params.minCircularity = 0.05

# no circularity needed
params.filterByCircularity = False

params.filterByConvexity = True

params.filterByInertia = False


detector = cv2.SimpleBlobDetector_create(params)

keypoints = detector.detect(frame)
im_with_keypoints = cv2.drawKeypoints(frame, keypoints, np.array([]), (125,0,0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)



cv2.imshow("Keypoints", im_with_keypoints)


d=0
for k in keypoints:
    d+=1

    (x,y) = k.pt
    x = int(round(x))
    y = int(round(y))
    s=k.size
    s=int(round(s))
    a=int(round(x+(s/2))+4)
    b=int(round(y+(s/2))+4)
    c = int(round(x - (s / 2))-2)
    d = int(round(y - (s / 2))-2)

    cv2.rectangle(frame,(a,b), (c,d), (0,0,0),3)
    cv2.imshow("with frame", frame)

    #Mat cropedImage = fullImage(Rect(X,Y,Width,Height));
    #frame=cv2.copyMakeBorder(frame,a,d,c,b, cv2.BORDER_REPLICATE)
    #frame = frame[int(y-7):int(y+7),int(x-7):int(x+7)]
    #frame = cv2.resize(frame, (30,30))
    #cv2.imshow("frame", frame)
    
    
    # sharpening
    kernel = np.array([[-1,-1,-1],[-1, 9,-1],[-1,-1,-1]])
    sharpened = cv2.filter2D(frame, -1, kernel)        
    # cv2.imshow("sharpenned",sharpened)
    # img blur
    img = cv2.medianBlur(frame,3)
    
    ret,bina = cv2.threshold(img,150,255,cv2.THRESH_BINARY)        
    th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
    cv2.THRESH_BINARY,11,2)

    print("pornees")

    # cv2.imshow("binary", bina)
    # cv2.imshow("sharp", sharpened)
    # cv2.imshow("adaptive",th3)
    
    image_rot(frame)

    # text = pytesseract.image_to_string(frame)
    # #os.remove(filename)
    # print("Text detected",text)

    # show the output images

 

cv2.waitKey(0)
cv2.destroyAllWindows()



