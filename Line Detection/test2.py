#Load image
import cv2
import numpy as np
frame = cv2.imread('src.jpg')
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

#Lift Blue.
lower_blue = np.array([60, 40, 40])
upper_blue = np.array([150, 255, 255])
mask = cv2.inRange(hsv, lower_blue, upper_blue)

#Detect edges
edges = cv2.Canny(mask, 200, 400)

