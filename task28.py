"""
Problem Statement:  WAP to read your image and display the following images
                    0. Show the original image
                    1. A Gray Scale Image
                    2. A Color Image Half the Size of the Original Image
                    3. Add a RED rectangular border arround the image
                    4. Put your name on the image in Green Color

Given: products.db with 20 product data
OUTPUT:

Author:             Prof. Shiburaj
"""
import cv2 as cv


img = cv.imread('shibufull.jpg',1)
height, width, dim = img.shape
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
small = cv.resize(img, (0, 0), fx=0.5, fy=0.5)
border = img.copy()
border = cv.rectangle(border, (0,0), (width, height), (0,0,255), 5)
textImg = img.copy()
(label_width, label_height), baseline = cv.getTextSize("Shiburaj", fontFace=cv.FONT_HERSHEY_PLAIN, fontScale=3, thickness=3)
textImg = cv.putText(textImg, text="Shiburaj", color=(0,255,0), org=(int(width/2 - label_width/2),int(height - label_height)), fontFace=cv.FONT_HERSHEY_PLAIN, fontScale=3, thickness=3)
cv.imshow('Input', img)
cv.imshow('Gray Scale', gray)
cv.imshow('Resized Image', small)
cv.imshow('Bordered Image', border)
cv.imshow('Text Image', textImg)
cv.imwrite('shibu2.png', gray)
cv.waitKey(0)
cv.destroyAllWindows()