from CarVision import detect_lane
from CarVision import display_lines

from datetime import datetime, date
import cv2

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
#return lane_lines_image