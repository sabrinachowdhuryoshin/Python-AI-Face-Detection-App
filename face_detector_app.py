import cv2

# load the cascade
# haarcascade algorithm only takes the gray scale images
trained_face_data = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# choose an image to detect faces in
img = cv2.imread("Robert-Downey-Jr.png")

cv2.imshow("Clever Programmer Face Detector", img)
cv2.waitKey(1000)

print("Code Completed")