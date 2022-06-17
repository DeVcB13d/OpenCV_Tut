'''
contours - edges of an image
'''
import cv2 as cv
import numpy as np


img = cv.imread('Photos/lady.jpg')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
blur = cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)
canny = cv.Canny(blur,125,175)


contours, hierachies = cv.findContours(canny,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
'''
mode to find:
RETR_LIST = returns all contours
RETR_EXT = external contours
RETR_TREE = returns hierachical contours

contour approx - 
CHAIN_APPROX_NONE - no change
CHAIN_APPROX_SIMPLE
looks at the structuring elements and returns the edges

'''
print("contours  : " , len(contours))


cv.imshow('Gray',canny)

blank = np.zeros(img.shape,dtype='uint8')
cv.drawContours(blank,contours,-1,(0,0,255),2)
cv.imshow('BLank',blank)
cv.waitKey(0)