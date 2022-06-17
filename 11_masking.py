import cv2 as cv
import numpy as np
'''
MAsking - To focus on essential part of the image only
'''
img = cv.imread('Photos/park.jpg')

blank = np.zeros(img.shape[:2],dtype = "uint8")
mask= cv.circle(blank,(img.shape[1]//2+10,img.shape[0]//2),100,255,-1)
cv.imshow("MAsk",mask)
mask_image = cv.bitwise_and(img,img,mask = mask)
cv.imshow("MAsked image",mask_image)

cv.waitKey(0)