import numpy as np
import cv2
import time


cap = cv2.VideoCapture(0)
count = 0
found = 'Nothing'
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    

    
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
   

    #ret,thresh = cv2.threshold(gray,127,255,1)
    ret,thresh = cv2.threshold(gray,100,255,1)
 
    contours,h = cv2.findContours(thresh,1,2)

    
    for cnt in contours:
        approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
        #print(len(approx))
        if len(approx)==5:
            found = "pentagon"
            cv2.drawContours(frame,[cnt],0,255,-1)
        elif len(approx)==3:
            found = "triangle"
            cv2.drawContours(frame,[cnt],0,(0,255,0),-1)
        elif len(approx)==4:
            found = "square"
            cv2.drawContours(frame,[cnt],0,(0,0,255),-1)   
        elif len(approx) == 9:
            found = "half-circle"
            cv2.drawContours(frame,[cnt],0,(255,255,0),-1)
        elif len(approx) > 15:
            found = "circle"
            cv2.drawContours(frame,[cnt],0,(0,255,255),-1)
            
    cv2.imshow("preview", thresh)
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break
   
    count += 1
    if count %  10  == 0:
        print(found)
    

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()



