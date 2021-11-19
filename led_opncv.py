#!/usr/bin/env python3
import cv2
import numpy as np
#import imutils
# Simple test for NeoPixels on Raspberry Pi
import time
import board
import neopixel


# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board>
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D18

# The number of NeoPixels
num_pixels = 100

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green>
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.8, auto_write=False, pixel_order=ORDER)

# Reverse LEDs
def reverse(seq, start, stop):
    size = stop + start
    for i in range(start, (size + 1) // 2 ):
        j = size - i
        seq[i], seq[j] = seq[j], seq[i]

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
    print(color)
    for color_led in range(len(color)):
        if color[color_led]> 0:
            pixels[color_led] = (0,0,0)
        else:
            pixels[color_led] =(255,255,255)
    pixels.show()
    cv2.imshow('frame',dst)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
