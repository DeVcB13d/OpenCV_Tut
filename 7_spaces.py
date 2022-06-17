"""
Space of colors - RGB,grayscale,HSV to represent an image
"""
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('Photos/lady.jpg')
#RGB to grayscale

#matplotlib takes an inverted rgb image
#need to convert it to BGR to show it in normal format
plt.imshow(img)
plt.show()

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#cv.imshow("gray",gray)

#BGR to HSV - hue saturation value
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
#cv.imshow("hsv",hsv)

lab = cv.cvtColor(img,cv.COLOR_BGR2LAB)
#cv.imshow("lab",lab)

rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)
plt.imshow(rgb)
plt.show()
cv.waitKey(0)