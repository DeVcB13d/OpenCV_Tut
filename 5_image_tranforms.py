import cv2 as cv
import numpy as np

img = cv.imread('Photos/park.jpg')

#To shift the image
def translate(img,x,y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimensions)

#rotating the image
def rotate(img, angle,retPoint = None):
    (height,width) = img.shape[:2]

    if rotPoint == None:


translated  = translate(img,-100,100)
cv.imshow('translated',translated)
cv.waitKey(0)