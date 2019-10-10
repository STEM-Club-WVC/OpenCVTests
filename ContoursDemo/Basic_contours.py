import numpy as np
import cv2 as cv
im = cv.imread('test.png')
imgray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(imgray, 127, 255, 0)
contours, hierarchy = cv.findContours(thresh, 1, 2)


cv.line(im, (contours[0][0][0][0],contours[0][0][0][1]), (contours[0][1][0][0],contours[0][1][0][1]), (0,255,0),8)
print(contours)
print('Hierarchy')
print(hierarchy)
cv.imshow("preview", thresh)
