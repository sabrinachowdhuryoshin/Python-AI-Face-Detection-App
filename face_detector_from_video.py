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

cap = cv2.VideoCapture(str(media_path) + "\\love.mp4")

# %%
while True:
    ret, frame = cap.read()
    if ret == True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame',gray)

        if cv2.waitKey(30) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()