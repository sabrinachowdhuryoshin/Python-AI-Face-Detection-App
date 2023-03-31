import cv2
from random import randrange

# load the cascade
# haarcascade algorithm only takes the gray scale images
trained_face_data = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# choose an image to detect faces in
# img = cv2.imread("Robert-Downey-Jr.png")
img = cv2.imread("Multiple_Faces_01.jpg")

# show the image 
cv2.imshow("Clever Programmer Face Detector", img)
cv2.waitKey(1000)

# must convert to grayscale
grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# show the grayscaled image
cv2.imshow("Clever Programmer Face Detector", grayscaled_img)
cv2.waitKey(1000)

# detect faces
face_coordinates  = trained_face_data.detectMultiScale(grayscaled_img)

# draw rectangles around the faces
# (x,y) - upper left point
# (x+w, y+h) - bottom right point
# 2 - thickness of the rectangle
# get the face coordinates dynamically
for (x,y,w,h) in face_coordinates:

    cv2.rectangle(img, (x,y), (x+w, y+h), (randrange(256), randrange(256), randrange(256)), 2)

# print(face_coordinates)

# display the image with the faces
cv2.imshow("Clever Programmer Face Detector", img)
cv2.waitKey(1000)

print("Code Completed")