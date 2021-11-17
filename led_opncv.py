import cv2
import numpy as np
import imutils

cap = cv2.VideoCapture(0)
#trackbar callback fucntion does nothing but required for trackbar
def nothing(x):
	pass
#create a seperate window named 'controls' for trackbar
cv2.namedWindow('controls')

#create trackbar in 'controls' window with name 'r''
cv2.createTrackbar('control_lower','controls',15,255,nothing)
cv2.createTrackbar('control_upper','controls',15,255,nothing)

while(True):
    # Capture frame-by-frame
    
    ret, frame = cap.read()
   
    #frame = imutils.resize(frame,80, 60)
    frame =cv2.resize(frame,(10, 10), interpolation = cv2.INTER_LINEAR)
    print(frame.shape)
    # Define sliders on the slider image
    threshold_lower= int(cv2.getTrackbarPos('control_lower','controls'))
    threshold_upper= int(cv2.getTrackbarPos('control_upper','controls'))
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Thresholding using THRESH_BINARY_INV 
    #th, dst = cv2.threshold(gray,threshold_lower, threshold_upper, cv2.THRESH_BINARY_INV); 
    #Basic threshold example 
    th,dst = cv2.threshold(gray, threshold_lower, threshold_upper, cv2.THRESH_BINARY);
    print("Shape", dst.shape)
    #pixel_color = frame.sum(axis=2)
    # Print RGB values for the image
    color = []
    for x in range (0,10,1):
        for y in range(0,10,1):
            pixel_color = int(dst[y,x])
            color.append(pixel_color)
            print (color)
    for change_pixel in range(0,len(color)):
        if (pixel_color >= 1):
            #Set led to black
            print("LED Black", pixel_color)
        else:
            # Set pixel to white
            print("LED White", pixel_color)
            # Check color, if its all zeroes then turn on the approriate LED to white
            # Things to do..change x,y pixel cordinates to location on the strip
    
    cv2.imshow('frame',dst)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
