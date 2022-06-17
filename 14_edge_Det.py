# Edges - gradients

import cv2 as cv
import numpy as np

img = cv.imread("Photos/park.jpg")
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# Laplacian - Computes gradients 

lap = cv.Laplacian(gray,cv.CV_64F)
lap = np.uint8(np.absolute(lap))

cv.imshow("Laplacian",lap)

# Sobel gradient

sobelx = cv.Sobel(gray,cv.CV_64F,1,0)
sobely = cv.Sobel(gray,cv.CV_64F,0,1)
sum = cv.bitwise_and(sobelx,sobely)

cv.imshow("Sobelx",sobelx)
cv.imshow("Sobely",sobely)
cv.imshow("combSobely",sum)

# Canny - more advanced algorithm to get the edges
canny = cv.Canny(gray,15,175)
cv.imshow("Canny",canny)

cv.waitKey(0)