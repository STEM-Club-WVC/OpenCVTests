import cv2
import numpy as np

print("Starting image assesment(" + "src.jpg" + ")")

#First, get the gray image and process GaussianBlur.
img = cv2.imread('src.jpg')

#isolate all the blue areas on the image
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

#Now we can “lift” all the blueish colors from the image
lower_blue = np.array([60, 40, 40])
upper_blue = np.array([150, 255, 255])
mask = cv2.inRange(hsv, lower_blue, upper_blue)

#Collect edges
edges = cv2.Canny(mask, 200, 400)


print("Finished.")

cv2.imshow('image', mask)
cv2.waitKey()
