import cv2 as cv
import numpy as np

img = cv.imread("Photos\group 1.jpg")
cv.imshow("Group",img)

#Splitting int its 3 color components

b,g,r = cv.split(img)
'''
THe result is a BW distribution
that becomes lighter as we are more close to the color
'''
cv.imshow("blue",b)
cv.imshow("green",g)
cv.imshow("red",r)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

blank = np.zeros(img.shape[:2],dtype = 'uint8')
blue = cv.merge([b,blank,blank])
red = cv.merge([r,g,blank])
cv.imshow("RED",red)
#Merges all the color channels to create the original image
merged = cv.merge([b,g,r])

cv.waitKey(0)