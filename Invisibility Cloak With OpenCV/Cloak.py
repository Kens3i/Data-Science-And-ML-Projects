# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 14:39:07 2021

@author: Koustav Banerjee
"""

import numpy as np
import cv2
import time


print("!! Invisibility is no more a Dream !!")

#as it is connected to only one webcam
cap = cv2.VideoCapture(0)

time.sleep(3)
#to adjust the cam

count = 0

background = 0


#Capturing Background
for i in range(60):

    ret, background = cap.read()
    #captures background 30 times so best image of background is being captured
    #also returns if the return value is true or false


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

     #saturation is the darkness of color
    lower_red = np.array([0, 120, 70])
    
    #below 70 brighness will be really low so it will hamper the color
    upper_red = np.array([10, 255, 255])
    
    #mask1 will be hiding those colors which are very dark
    #mask1 will be separating the clock park
    mask1 = cv2.inRange(hsv, lower_red, upper_red)
    
    
    lower_red = np.array([170, 120, 70])
    upper_red = np.array([180, 255, 255])
    mask2 = cv2.inRange(hsv, lower_red, upper_red)
    #red color is again red color
    
    mask1 = mask1 + mask2
    #OR 1 or x, bitwise operator
    #will mask those red color if its either in mask1 or mask2
    
    
    #morph will be removing the noise and make it more refined
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8), iterations=2)
    
    #Increasing the smoothness
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_DILATE, np.ones((3, 3), np.uint8), iterations=1)

    mask2 = cv2.bitwise_not(mask1)
    #everything except the cloak

    res1 = cv2.bitwise_and(background, background, mask = mask1)
    #segmentation of color
    
    res2 = cv2.bitwise_and(img, img, mask = mask2)
    #substitute the cloak part
    
    #linearly add 2 images
    final_output = cv2.addWeighted(res1, 1, res2, 1, 0)

    cv2.imshow('Koustav's Project' !!', final_output)
    k = cv2.waitKey(10)
    if k == 27:
        break
    
     #Pressing the escape key will result in end

cap.release()
cv2.destroyAllWindows()