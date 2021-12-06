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
num_pixels = 64

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green>
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.1, auto_write=True, pixel_order=ORDER)

# Reverse LEDs
def reverse(seq, start, stop):
    size = stop + start
    for i in range(start, (size + 1) // 2 ):
        j = size - i
        seq[i], seq[j] = seq[j], seq[i]

cap = cv2.VideoCapture(0)


while(True):
    # Capture frame-by-frame
   
    ret, frame = cap.read()
   
    #frame = imutils.resize(frame,80, 60)
    frame =cv2.resize(frame,(8, 8), interpolation = cv2.INTER_LINEAR)

    (b, g ,r) =frame[4,4]

    # Our operations on the frame come here

    position = 0
    color = []
    for x in range (0,8,1):
        for y in range(0,8,1):
            (b, g, r) = frame[y,x]
            color.insert(position,(r,g,b))
            position = position +1
    for X1 in range(len(color)):
        pixels[X1] = color[X1]   
            
   # cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
