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

# %%
sample_video = cv2.VideoCapture(str(media_path) + "\\love.mp4")

# iterate forever over frames
while True:

    # read the current frame
    successful_frame_read, frame = sample_video.read()

    # must convert to grayscale
    grayscaled_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
   
    # detect faces
    face_coordinates  = trained_face_data.detectMultiScale(grayscaled_frame)
    # print(face_coordinates) # debug

    # get the face coordinates dynamically
    for (x,y,w,h) in face_coordinates:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (randrange(256), randrange(256), randrange(256)), 2)

    # show the video
    cv2.imshow("Sabrina Chowdhury's Face Detector App", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
            break

sample_video.release()

# %%
print("\nCode Completed!\n")