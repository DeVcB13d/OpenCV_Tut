import cv2 as cv

#read an image
img = cv.imread('Photos/cat.jpg')


#show the image
cv.imshow('cat',img)
#display for a certain time
cv.waitKey(0)


#reading videos
capture = cv.VideoCapture('videos/dog.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video',frame)
    #When d is pressed the video exits
    if cv.waitKey(20) & 0xFF == ord('d'):
        break
capture.release()
cv.destroyAllWindows()
