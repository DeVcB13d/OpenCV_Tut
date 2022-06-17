import cv2 as cv
from numpy import average

img = cv.imread("Photos\group 1.jpg")


'''
Blurring reduces the noise in the image
Averaging  : 
Pixel intensity in a region is reduced to avg of ts surrounding pixels
The (3,3) ,(7,7) is known as the kernel size , and its the traversing agent
'''
# Averaging
average = cv.blur(img,(3,3))
cv.imshow("avg blur",average)

# Gaussian blur
gauss = cv.GaussianBlur(img,(3,3),0)
cv.imshow("Gauss",gauss)

# Median blur - the median in surrounding pixels is reduced in comparison
# to averaging
m = cv.medianBlur(img,3)
cv.imshow("MEdian",m)

# Bilateral
bilateral = cv.bilateralFilter(img,10,35,25)
cv.imshow("bil",bilateral)

cv.waitKey(0)