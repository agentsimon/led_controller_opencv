import serial
import time
import cv2

import argparse  

#The following line is for serial over GPIO
port = '/dev/cu.usbmodem142301' # note I'm using Mac OS-X


ard = serial.Serial(port,9600,timeout=5)
time.sleep(2) # wait for Arduino

vid = cv2.VideoCapture(0)



""" def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data """

while(True):
      
    # Capture the video frame
    # by frame
    
    ret, frame = vid.read()
    frame =cv2.resize(frame,(8, 8), interpolation = cv2.INTER_LINEAR)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _,thres_image = cv2.threshold(gray, 120,255,0)
    # Display the resulting frame
    #print(thres_image)
    cv2.imshow('frame', thres_image)

    res =thres_image
    for line in enumerate(thres_image):
        for index2 in enumerate(thres_image[line[0]]):
            if thres_image[line[0]][index2[0]] > 0:
                res[line[0]][index2[0]] = 1

    #print(res) 
    #print(type(res))  
    list1 = res.tolist()
    #value = write_read(list1)
    complete_list=[]
    for i in list1:
        for j in i:
            complete_list.append(j)
    print("List is ", complete_list)
    list_numbers_string = "".join(str(string_list) for string_list in complete_list)
    print("String is", list_numbers_string)
    ard.flush()
    print ("Python value sent: ", list_numbers_string)
    ard.write(str.encode(list_numbers_string))
    time.sleep(1)
    # Serial read section
    msg = ard.read(ard.inWaiting()) # read all characters in buffer
    print ("Message from arduino: ")
    print (msg)       
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  
# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()
