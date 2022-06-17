import cv2 as cv

img = cv.imread('Photos/group 1.jpg')


gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

#Reads the xml face
haar_cascade = cv.CascadeClassifier('haar_face.xml')
#Returns coordinates of rectangle with FACe
faces_rect = haar_cascade.detectMultiScale(gray,scaleFactor = 1.1,minNeighbors=1)

print("Number of faces found = ",{len(faces_rect)})

for x,y,w,h in faces_rect:
    cv.rectangle(img,(x,y),(x+w,x+h),(0,233,0),thickness=2)
cv.imshow('Lady',img)

cv.waitKey(0)