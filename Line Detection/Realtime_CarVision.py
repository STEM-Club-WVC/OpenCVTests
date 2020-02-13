import cv2
import numpy as np
import logging
from datetime import datetime, date

from picamera.array import PiRGBArray
from picamera import PiCamera
import time

from CarVision import detect_lane
from CarVision import display_lines
from CarVision import show_process_frame


# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))

# allow the camera to warmup
time.sleep(0.1)

# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):

    # grab the raw NumPy array representing the image, then initialize the timestamp
    # and occupied/unoccupied text
    image = frame.array
    # show the frame
    #cv2.imshow("Frame", image)
    show_process_frame(image)
    key = cv2.waitKey(1) & 0xFF
    # clear the stream in preparation for the next frame
    rawCapture.truncate(0)
    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break

cv2.waitKey()

#record starttime
starttime = datetime.now()
show = True
#Import image
frame = cv2.imread('src.jpg')

lane_lines = detect_lane(frame)

lane_lines_image = display_lines(frame, lane_lines)

#create scaler
scale_percent = 35 # percent of original size
width = int(frame.shape[1] * scale_percent / 100)
height = int(frame.shape[0] * scale_percent / 100)
dim = (width, height)
# resize image
lines_edges_downscaled = cv2.resize(lane_lines_image, dim, interpolation = cv2.INTER_AREA)

# resize image
frame_downscaled = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)

finishtime = datetime.now()
runtime = finishtime - starttime
print("Runtime: ", runtime);

if(show):
    cv2.imshow("Source Image", frame_downscaled)
    cv2.imshow("lane lines", lines_edges_downscaled)
    cv2.waitKey()#cv2.imshow() will fail unless it enters waitKey right after.
