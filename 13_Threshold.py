'''
TO convert an image to binary 0 / 255
set a threshold and elements below thresh are 0 and
and others are 1
'''
#Simple Thresholding
import cv2 as cv

img = cv.imread("Photos/park.jpg")
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

#Simple thresholding
#150 - Threshold value
#255 - maximum value
#Thresholding type
#Returns - threshold - value, thresh - imag

threshold,thresh = cv.threshold(gray,150,255,cv.THRESH_BINARY)
cv.imshow("Thresh",thresh)

threshold,thresh_inv = cv.threshold(gray,150,255,cv.THRESH_BINARY_INV)
cv.imshow("Thresh2",thresh_inv)

# Adaptive thresholding - caluclates adaptive value based on mean/
# 11 - block size
# 3 -  t
adptive_thresh = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C
,cv.THRESH_BINARY_INV,11,3)

cv.imshow("Adaptive Thresh",adptive_thresh)
cv.waitKey(0)