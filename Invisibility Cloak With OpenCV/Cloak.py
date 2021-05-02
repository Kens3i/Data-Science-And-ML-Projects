# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 14:39:07 2021

@author: Koustav Banerjee
"""

import numpy as np
import cv2
import time


print("!! Activating Invisibility Cloak !!")

#as it is connected to only one webcam
cap = cv2.VideoCapture(0)

#to adjust the cam
time.sleep(3)

count = 0
background = 0

#Capturing Background
for i in range(60):

    ret, background = cap.read()
    #captures background 60 times so best image of background is being captured
    #also returns if the return value is true or false("ret")


# Flip the Image
background = np.flip(background, axis=1)

#To make sure the code is running till the webcam is turned on
while(cap.isOpened()):

    ret, img = cap.read()
    #Returning image to perform operation on it

    if not ret:
        break

    count+=1
    img = np.flip(img, axis=1)

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    #Converts the color from rgb to hsv(hue saturation value)
    #as in hsv hue is there and the color depends on the angle of light
    #hsv=Hue saturation value
    #There is a problem in OpenCv that its 8 bits so 255, but hsv has 360 degrees of colors
    #So we have reduced the 360 degrees to 180 degree and increased the color variation wrt change in angle

    #saturation is the darkness of color
    lower_red = np.array([0, 100, 30])
    #0 degree is H i.e Hue, 120 is S i.e Saturation or Darkness of color,and V is the brightness of the color

    #below 70 brightness will be really low so it will hamper the color
    upper_red = np.array([10, 255, 255])

    #mask1 will be hiding those colors which are very dark
    #mask1 will be separating the clock part
    mask1 = cv2.inRange(hsv, lower_red, upper_red)
    
    
    lower_red = np.array([170, 100, 30])
    upper_red = np.array([180, 255, 255])
    mask2 = cv2.inRange(hsv, lower_red, upper_red)
    #here we are just checking the red color present between 170-180 degrees in the hue scale
    
    mask1 = mask1 + mask2
    # + is OR i.e bitwise operator
    #will segment those red color if its either in mask1 or mask2
    
    
    #morph will be removing the noise and make img more refined
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8), iterations=2)
    #morphologyEX(the img,morphological func,kernel,how many we want to apply the operation)
    
    #Increasing the smoothness
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_DILATE, np.ones((3, 3), np.uint8), iterations=1)

    mask2 = cv2.bitwise_not(mask1)
    #everything except the cloak

    res1 = cv2.bitwise_and(background, background, mask = mask1)
    #segmentation of color from the rest of the thing
    
    res2 = cv2.bitwise_and(img, img, mask = mask2)
    #substitute the cloak part, img = captured when we are at the front of the camera
    
    #linearly add 2 images
    final_output = cv2.addWeighted(res1, 1, res2, 1, 0)
    #alpha times res1 + beta times res 2 + gamma

    cv2.imshow("Invisibility Cloak Activated' !!", final_output)
    k = cv2.waitKey(10)
    if k == 27:
        break
    
     #Pressing the escape key will result in end

cap.release() #ended the object cap
cv2.destroyAllWindows() #window will be closed