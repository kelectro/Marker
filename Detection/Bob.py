import cv2
import numpy as np


# img = cv2.imread('test.png', cv2.IMREAD_GRAYSCALE)
width=640
height=480
# img=cv2.resize(img,(width,height))

#im = cv2.GaussianBlur(img,(5,5),0)

cap = cv2.VideoCapture('samplevideo.mp4')
p=0
#while True :
while cap.isOpened():
    ret, frame = cap.read()
    #frame=cv2.resize(frame, (640, 480), fx=0, fy=0, interpolation=cv2.INTER_NEAREST)
    frame=cv2.resize(frame,(width,height))
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame',frame)
    #to save the frame
    #we can use it at the detection to keep save it
    #cv2.imwrite("frame%d.jpg" % p, frame)
    #img= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    p=p+1
    print('frame no.',p)

# Simple blob detector
    params = cv2.SimpleBlobDetector_Params()

    # set threshold
    params.minThreshold = 10
    params.maxThreshold = 200

    # Area filtering
    params.filterByArea = True
    params.minArea =75
    params.maxArea = 250

    # no circularity needed
    params.filterByCircularity = False
    params.filterByConvexity = True

    params.filterByInertia = False
    # opencv version 4
    # for older version <3
    # use detector = cv2.SimpleBlobDetector(params)

    detector = cv2.SimpleBlobDetector_create(params)

    keypoints = detector.detect(frame)


    # Draw detected blobs as red circles.
    # cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures
    # the size of the circle corresponds to the size of blob

    im_with_keypoints = cv2.drawKeypoints(frame, keypoints, np.array([]), (125,0,0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    # Show blobs
    cv2.imshow("Keypoints", im_with_keypoints)
    print("p=",p)
    key = cv2.waitKey(50) & 0xFF
    #cv2.waitKey(100)
    if key == ord("q"):
        break
        #to extract more info about the blobs
        #https://stackoverflow.com/questions/13534723/how-to-get-extra-information-of-blobs-with-simpleblobdetector
        # for (std
        # ::vector < cv::KeyPoint >::iterator blobIterator = myBlobs.begin(); blobIterator != myBlobs.end(); blobIterator++){
        # std::
        #     cout << "size of blob is: " << blobIterator->size << std::endl;
        # std::cout << "point is at: " << blobIterator->pt.x << " " << blobIterator->pt.y << std::endl;
        # }

    cap.release()
cv2.destroyAllWindows()
