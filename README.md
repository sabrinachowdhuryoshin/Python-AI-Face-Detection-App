# Python AI Face Detection App

This GitHub project demonstrates simple python based applications that use machine learning algorithms to detect faces in images, live webcam feeds, and videos.

# Features
- Can detect faces in static images or in live webcam feeds
- Can also detect faces in pre-recorded videos
- Uses a pre-trained machine learning model for high accuracy face detection
- Includes a simple user interface for ease of use
- Can be easily modified to suit specific use cases

# Requirements
- Python 3.x
- OpenCV
- Haar Cascade Classifier XML file (included in the repository)

# Installation
- Clone the repository or download the source code
- Install the required packages using pip: `pip install opencv-python`
- Run the application using the command `python face_detector_from_webcam.py`
  
# Usage

- The application can be used to detect multiple faces in images, live webcam feeds, and videos.

- To detect faces in an image, simply change the name of the image from the `trained_face_data` variable and choose an image from the `media` folder. The application will display the image with the detected faces outlined in muiltple random colors.

- To detect faces in a video, simply change the name of the video from the `trained_face_data` variable and choose a video from the `media` folder. The application will play the video with the detected faces outlined in in muiltple random colors. To stop the video feed, poress the `q` button.

- To detect faces in a live webcam feed, just run the module. The application will open your computer's default camera and begin detecting faces in real-time. To stop the webcam feed, poress the `q` button.

# Customization
This application can be easily customized to suit specific use cases. To do so, you can modify the individual `.py` files to include additional functionality, or modify the `haarcascade_frontalface_default.xml` file to train the model on a different set of faces.

# License
This project is licensed under the Unlicense - see the `LICENSE.md` file for details.
