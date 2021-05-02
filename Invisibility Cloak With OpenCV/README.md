# Invisibility Cloak
## Python App Developed with OpenCV 

## Table of Contents

1.  [Overview](https://github.com/Kens3i/Data-Science-And-ML-Projects/tree/main/Invisibility%20Cloak%20With%20OpenCV#Overview)
    
2.  [Motivation](https://github.com/Kens3i/Data-Science-And-ML-Projects/tree/main/Invisibility%20Cloak%20With%20OpenCV#Motivation)
    
3.  [Libraries Used](https://github.com/Kens3i/Data-Science-And-ML-Projects/tree/main/Invisibility%20Cloak%20With%20OpenCV#Libraries-Used)
    
4.  [Workflow](https://github.com/Kens3i/Data-Science-And-ML-Projects/tree/main/Invisibility%20Cloak%20With%20OpenCV#Workflow)

5.  [Screenshots](https://github.com/Kens3i/Data-Science-And-ML-Projects/tree/main/Invisibility%20Cloak%20With%20OpenCV#Screenshots)

6. [FAQs](https://github.com/Kens3i/Data-Science-And-ML-Projects/tree/main/Invisibility%20Cloak%20With%20OpenCV#FAQs)


## Overview

This is simply a program that uses **image segmentation** and **image processing** to replace the foreground object of interest with the background. Only the **`red` color** will get **invisible** and we will be seeing the background instead of any red object. We are capturing the **live feed** of the person and breaking that feed into images, basically frames. On those frames we will apply **image segmentation** to differentiate the color of the object from rest of the image and we then super-impose the background image over there.<br>
**Basically this [app]() turns a `red` colour cloth into an invisibility cloak**.

## Motivation

I always had a childhood fantasy of using an invisibility cloak. Well it turns out that using simple image processing tricks I can now actually fulfill my childhood fantasy. Also this project help me develop my image processing and OpenCV skills.

## Libraries-Used

-   `numpy`
-   `cv2`
-   `time`


## Workflow

- **Capturing Background**

- **Converting** RGB to HSV.

- **Selecting** a range, which is used to segment the colors.

- Creating a **mask** with the segmented HSV color which will be **separating** the **red color** from the rest.

- Applying **Morphological Operations**(Opening and Dialation) to fill out holes in the mask.

- **Morphological Opening** will be removing the noise and make img more refined.

- **Morphological Dialate** will increase the smoothness.

- Creating **another mask** which contains everything except the red color (Using bitwise_not).

- Creating **two results**, one for the mask 1 and background and the other for the mask 2 and the image.

- Finally **adding both** the results to get the suitable output.

## Screenshots
![]()
PS: Sometimes Due To Not Enough Lighting The Edges Get Distorted.


## Challenges I Faced

- This was my 1st full fleged image processing project so I had to lookup for the syntax of  `OpenCV` in the documentation and learn its basic functions.

- Sometimes the app won't work properly as my room is not that well litted. Due to less light the brightness of my cloak got affected and the red color became to dark to detect.

- It took me some more time to learn about morphological operations, masking and image segmentation.


## FAQs
### What is Image Processing ?
Image Processing means processing digital image by means of a digital computer. We can also say that it is a use of computer algorithms, in order to get enhanced image either to extract some useful information.

### What is `OpenCV` ?
OpenCV is the huge open-source library for the computer vision, machine learning, and image processing and now it plays a major role in real-time operation which is very important in today’s systems.

### Understanding kernel
Kernels in computer vision are matrices, used to perform some kind of convolution in our data. Let’s try to break this down.
Convolutions are mathematical operations between two functions that create a third function. In image processing, it happens by going through each pixel to perform a calculation with the pixel and its neighbours.

### What is Morphological Operations ?
Morphology is a broad set of image processing operations that process images based on shapes. In a morphological operation, each pixel in the image is adjusted based on the value of other pixels in its neighborhood. It needs two inputs, one is our original image, second one is called **structuring element** or **kernel** which decides the nature of operation. Two basic morphological operators are Erosion and Dilation.

### What is Erosion ?
The basic idea of erosion is just like soil erosion only, it erodes away the boundaries of foreground object. All the pixels near boundary will be discarded depending upon the size of kernel. So the thickness or size of the foreground object decreases or simply white region decreases in the image. It is useful for removing small white noises (as we have seen in colorspace chapter), detach two connected objects etc.

### What is Dialation ?
It is just opposite of erosion. Here, a pixel element is '1' if atleast one pixel under the kernel is '1'. So it increases the white region in the image or size of foreground object increases. Normally, in cases like noise removal, erosion is followed by dilation. Because, erosion removes white noises, but it also shrinks our object. So we dilate it. Since noise is gone, they won't come back, but our object area increases. It is also useful in joining broken parts of an object.

### What is Morphological Opening ?
Opening is just another name of **erosion followed by dilation**.

### Thankyou For Spending Your Precious Time Going Through This Project!
### If You Find Any Value In This Project Or Gained Something New Please Do Give A ⭐.
