# To reckognize faces in an image using opencv built 
# in face reckogniser

import os
import cv2 as cv
import numpy as np

people = []
for i in os.listdir(r"C:\Users\USER\Documents\GitHub\Image-Processing\Tutorial\opencv-course-master\opencv-course-master\Resources\Faces\train"):
    people.append(i)
print(people)
DIR = r"C:\Users\USER\Documents\GitHub\Image-Processing\Tutorial\opencv-course-master\opencv-course-master\Resources\Faces\train"
haar_cascade = cv.CascadeClassifier('haar_face.xml')
features = []
labels = []

def create_train():
    # Creating a training set
    for person in people:
        path = os.path.join(DIR,person)
        label = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path,img)
            img_array = cv.imread(img_path)
            gray_img = cv.cvtColor(img_array,cv.COLOR_BGR2GRAY)
            faces_rect = haar_cascade.detectMultiScale(gray_img,scaleFactor = 1.1,minNeighbors=4)
            for(x,y,w,h) in faces_rect:
                faces_roi = gray_img[y:y+h,x:x+w]
                features.append(faces_roi)
                labels.append(label)
create_train()
print("Features : ",len(features))
print("Labels : ",len(labels))

face_recognizer = cv.face.LBPHFaceRecognizer_create()

features =np.array(features,dtype='object')
labels = np.array(labels)

#Train the recognizer
face_recognizer.train(features,labels)

face_recognizer.save('face_trained.yml')
np.save("features.npy",features)
np.save("labels.npy",labels)
