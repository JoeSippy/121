# import cv2 to capture videofeed
import cv2

import numpy as np

# attach camera indexed as 0
camera = cv2.VideoCapture(0)

# setting framewidth and frameheight as 640 X 480
camera.set(3 , 640)
camera.set(4 , 480)

# loading the mountain image
mountain = cv2.imread('mount everest.jpg')


while True:

    # read a frame from the attached camera
    status , frame = camera.read()

    # if we got the frame successfully
    if status:

        # flip it
        frame = cv2.flip(frame , 1)

        # converting the image to RGB for easy processing
        frame_rgb = cv2.cvtColor(frame , cv2.COLOR_BGR2RGB)

        # creating thresholds
        lower_bound = np.array([100,100,100])
        upper_bound = np.array([255,255,255])

    lower_bound = np.array([0, 120, 50])
    upper_bound = np.array([10, 255,255])
    mask_1 = cv2.inRange( lower_bound, upper_bound)

    lower_bound= np.array([170, 120, 70])
    upper_bound = np.array([180, 255, 255])
    mask_2 = cv2.inRange( lower_bound, upper_bound)
    
    mask_1 = mask_1 + mask_2

    cv2.imshow("mask_1", mask_1)

    res_2 = cv2.bitwise_and(mountain,mountain,mask = mountain)
    final_output = cv2.addWeighted(mountain,1,mountain,1,0)
    camera.write(final_output)
       
        # show it
    cv2.imshow('frame' , frame)

        # wait of 1ms before displaying another frame
    code = cv2.waitKey(1)
    if code  ==  32:
            break

# release the camera and close all opened windows
camera.release()
cv2.destroyAllWindows()
