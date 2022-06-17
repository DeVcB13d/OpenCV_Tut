import cv2 as cv

def rescaleFrame(frame,scale = 0.75):
    #images,videos and live video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width,height)

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

def change_res(width,height):
    #it will change for live video only
    capture.set(3,width)
    capture.set(4,height)

#reading videos
capture = cv.VideoCapture('videos/video1.mp4')
f = 1
while True:
    #Getting the frame
    isTrue, frame = capture.read()
    #cv.imshow('Video',frame)
    #Getting a rescaled frame
    new_frame = rescaleFrame(frame,f)
    f = f+0.001
    cv.imshow('small video',new_frame)
    #When d is pressed the video exits
    if cv.waitKey(20) & 0xFF == ord('d'):
        break
capture.release()
cv.destroyAllWindows()

