#!/usr/bin/env python3
import cv2
import numpy as np
#import imutils
# Simple test for NeoPixels on Raspberry Pi
from time import sleep
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

# Check LEDs
wait = 1
sleep(wait)
pixels.fill((0, 255, 0))
pixels.show()
sleep(wait)
pixels.fill((0,0,255))
pixels.show()
sleep(wait)
pixels.fill((255,0,0))
pixels.show()
sleep(wait)
pixels.fill((0,0,0))
pixels.show()

# Define capture camera as USB
cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame 
    ret, frame = cap.read()
    # Resize the capured frame
    frame =cv2.resize(frame,(10, 10), interpolation = cv2.INTER_LINEAR)
    #print("Shape", frame.shape)
   
    # Print RGB values for the image
    color = []
    col_pos = [None] *100
    position = 0
    for x in range (0,10,1):
        for y in range(0,10,1):
            (b,g,r) = frame[y,x]
            position = position +1
            color.insert(position,(g,r,b))
    #print(color)
    
    for x in range(10,100,20):
        reverse(color, x, x+9)
    #print(color)
    for color_led in range(len(color)):
        pixels[color_led] = color[color_led]
        
    pixels.show()
    #cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
