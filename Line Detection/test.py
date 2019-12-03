import cv2
import numpy as np
from CarVision import *

showAllLines = True

print("Starting image assesment(" + "src.jpg" + ")")

img = cv2.imread('src.jpg')

#edges = detect_edges(img)
#croppedEdges = region_of_interest(edges)
#lineSegs = detect_line_segments(croppedEdges)
#lines = average_slope_intercept(img, lineSegs)

if(showAllLines):
    edges = detect_edges(img)

    lane_lines_image = display_lines(img, edges)

    cv2.imshow("lane lines", lane_lines_image)
else:
    laneLines = detect_lane(img)

    lane_lines_image = display_lines(img, laneLines)

    cv2.imshow("lane lines", lane_lines_image)
