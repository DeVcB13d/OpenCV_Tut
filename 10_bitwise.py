'''
Bitwise operators : operate in a binary manner
'''

import cv2 as cv
from cv2 import bitwise_and
from cv2 import bitwise_or
import numpy as np

blank = np.zeros((400,400),dtype = "uint8")
rectangle = cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)
circle = cv.circle(blank.copy(),(200,200),200,245,-1)
cv.imshow("Rectangle",rectangle)
cv.imshow("Circle",circle)

'''
THe operations would turn pixels on and off

'''

#Bitwise AND : intercesting
bitwise_and = cv.bitwise_and(rectangle,circle)
cv.imshow("AND",bitwise_and)

#Bitwise OR : common
B_or = cv.bitwise_or(rectangle,circle)
cv.imshow("OR",B_or)

#BITWise XOR : non intersecting
B_xor = cv.bitwise_xor(rectangle,circle)
cv.imshow("XOR",B_xor)

#NOT:
B_not = cv.bitwise_not(circle)
cv.imshow("NOT",B_not)

cv.waitKey(0)