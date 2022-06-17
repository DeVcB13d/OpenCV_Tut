'''
It helps in visualising pixel intensity distribution
'''
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('Photos/cats.jpg')

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
blank = np.zeros(img.shape[:2],dtype = 'uint8')
circle = cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),100,255,-1)
mask = cv.bitwise_and(gray,circle,mask = circle)
#ARG1 - list of images
#
#MAskinf
gray_hist = cv.calcHist([gray],[0],mask,[256],[0,256])
plt.figure()
plt.title("GrayScale Histogram")
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(gray_hist)
#plt.show()

#HISTOGRAM for RGB image
img = cv.imread('Photos/cats.jpg')
blank = np.zeros(img.shape[:2],dtype = 'uint8')
circle = cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),100,255,-1)
mask = cv.bitwise_and(gray,circle,mask = circle)

plt.figure()
plt.title("GrayScale Histogram")
plt.xlabel('Bins')
plt.ylabel('# of pixels')

colors = ('b','g','r')
for i,col in enumerate(colors):
    hist = cv.calcHist([img],[i],mask,[256],[0,256])
    plt.plot(hist,color=col)
    plt.xlim([0,256])
plt.show()
cv.waitKey(0)