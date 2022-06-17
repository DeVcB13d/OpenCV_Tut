import cv2 as cv
import numpy as np

#creating a blank image
# uint 8 is the image datype
blank = np.zeros((500,500,3),dtype='uint8')

#Painting the image a color
blank[200:300,300:400] = 34,56,25

cv.imshow('blank',blank)
#drawing a  rectangle
cv.rectangle(blank,(2,33),(90,90),(78,255,0),thickness=-2)
#Drawing a circle
cv.circle(blank,(45,55),56,(225,45,24),thickness=-1)
#Drawing a line
cv.line(blank,(100,40),(300,500),(225,45,24),thickness=5)
#Writing text onto an image
cv.putText(blank,"Hello",(250,200),cv.FONT_HERSHEY_PLAIN,6.0,(0,255,0),3)
cv.imshow('blank',blank)
cv.waitKey(0)