import cv2 as cv

img = cv.imread('Photos/TS2.jpg')
cv.imshow('Cat',img)
"""
#convert to greyscale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Grey',gray)
"""
#Blurring an image
blur = cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
#cv.imshow('Blur',blur)

#edge cascade
canny = cv.Canny(img,125,175)
#cv.imshow('Canny',canny)

#Dilating the image
dilated = cv.dilate(canny,(10,10),iterations=1)
#cv.imshow("dilated",dilated)

#eroding
eroded = cv.erode(dilated,(3,3),iterations=1)
#cv.imshow('eroded',eroded)

#Resize
img = cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow('Cat',img)
 
#Cropping
cropped = img[50:100,40:223]
cv.imshow('Crop',cropped)
cv.waitKey(0)
