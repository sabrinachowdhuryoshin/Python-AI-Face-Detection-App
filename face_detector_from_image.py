'''' standard python library '''

import os, cv2
from pathlib import Path
from random import randrange

# %%

'''' define directory paths '''

tool_path = os.path.dirname(os.path.abspath(__file__))
# print(tool_path) # debug

media_path = Path(tool_path + "\\media")
# print(media_path ) # debug

algorithm_path = Path(tool_path + "\\algorithm")
# print(algorithm_path ) # debug

# %%
# load the cascade algorithm
# haarcascade algorithm only takes the gray scale images
trained_face_data = cv2.CascadeClassifier(str(algorithm_path) + "\\haarcascade_frontalface_default.xml")
# print(trained_face_data) # debug

# choose an image to detect faces in
# img = cv2.imread(str(media_path) + "\\Robert_Downey_Jr.png")
# img = cv2.imread(str(media_path) + "\\Multiple_Faces_01.jpg")
img = cv2.imread(str(media_path) + "\\Multiple_Faces_02.jpg")
# print(img) # debug

# show the image 
cv2.imshow("Clever Programmer Face Detector", img)
cv2.waitKey(1000) # debug

# must convert to grayscale
grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# print(grayscaled_img) # debug

# show the grayscaled image
cv2.imshow("Clever Programmer Face Detector", grayscaled_img)
cv2.waitKey(1000) # debug

# %%
# detect faces
face_coordinates  = trained_face_data.detectMultiScale(grayscaled_img)
# print(face_coordinates) # debug

# draw rectangles around the faces
# (x,y) - upper left point
# (x+w, y+h) - bottom right point
# 2 - thickness of the rectangle
# get the face coordinates dynamically
for (x,y,w,h) in face_coordinates:
    cv2.rectangle(img, (x,y), (x+w, y+h), (randrange(256), randrange(256), randrange(256)), 2)

# display the image with the faces
cv2.imshow("Clever Programmer Face Detector", img)
cv2.waitKey(1000)

# %%
print("\nCode Completed!\n")