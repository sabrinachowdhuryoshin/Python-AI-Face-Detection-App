import cv2
from random import randrange

# load the cascade
# haarcascade algorithm only takes the gray scale images
trained_face_data = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# to capture video from webcam
webcam = cv2.VideoCapture[0]
# cv2.waitKey(1000)

print("Code Completed")