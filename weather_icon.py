# import the necessary packages
import numpy as np
import urllib
import cv2
import requests
import json
import urllib.request
import pygame
# METHOD #1: OpenCV, NumPy, and urllib to get the weather details
api_key = "a68a0ee8420eb5ffcb2a5ce643107da7"
lat = "10.075239"
lon = "108.224136"
location = "Turan"
url = "https://api.openweathermap.org/data/2.5/find?q={}&units=metric&appid={}".format(location, api_key)
response = requests.get(url)
data = json.loads(response.text)
#Print the weather dtails
print("Temperature is ", data["list"][0]["main"]["temp"])
print("Pressure is ", data["list"][0]["main"]["pressure"])
print("Humidity is ", data["list"][0]["main"]["humidity"])
print("Icon number is", data["list"][0]["weather"][0]["icon"])

# Get the weather icon
url = "https://openweathermap.org/img/wn/{}.png".format(data["list"][0]["weather"][0]["icon"])
#url = "https://openweathermap.org/img/wn/01d.png"
#url_response = urllib.request.urlopen(url)
#image = cv2.imdecode(np.array(bytearray(url_response.read()), dtype=np.uint8), -1)

resp = urllib.request.urlopen(url)
image = np.asarray(bytearray(resp.read()), dtype="uint8")
image = cv2.imdecode(image, cv2.IMREAD_COLOR)

#Change the icon to required image dimensions
height_image =22
width_image = 26
marginx = 10
marginy = 12
crop_img = image[marginy:marginy+height_image, marginx:marginx+width_image]
print("Size is", crop_img.shape)

# Set the pygame background colour and size
background_colour = (0,0,0)
(width, height) = (1000, 1000)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Weather')
screen.fill(background_colour)

pygame.display.flip()

running = True
while running:
    # Show original icon image
    cv2.imshow('Icon',image)
    # Show the croppedweather icon
    cv2.imshow('Cropped icon',crop_img)
    # Print out all the panels
    # First set an are to be white
    for x in range (1,100,1):
        for y in range(20,70,1):
            pygame.draw.circle(screen, (255,255,255), (x*10,y*10), 5)
   # Now print all the individual panes
   # Humidity Red        
    for x in range (14,24,1):
        for y in range(20,70,1):
            pygame.draw.circle(screen, (0,255, 0), (x*10,y*10), 5)
   # Temperature Blue        
    for x in range (2,12,1):
        for y in range(20,70,1):
            pygame.draw.circle(screen, (0,0,255), (x*10,y*10), 5)

    #  Weather icon
    for x1 in range (0,width_image,1):
        for y1 in range(2,height_image,1):
            #Get the color values from the icon image 
            (b,g,r) = crop_img[y1,x1]
            pygame.draw.circle(screen, (r,g,b), ((x1*10)+400,(y1*10)+300), 5)
     # Pollution Green        
    for x in range (77,87,1):
        for y in range(20,70,1):
            pygame.draw.circle(screen, (100, 100, 100), (x*10,y*10), 5)
    #  Air Presssure Blue
    for x in range (89,99,1):
        for y in range(20,70,1):
            pygame.draw.circle(screen, (14,140, 80), (x*10,y*10), 5)
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
