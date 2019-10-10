# Standard imports
import cv2
import numpy as np;

imageName = "blob.jpg"

# Read image
im = cv2.imread(imageName, cv2.IMREAD_GRAYSCALE)
 
# Set up the detector with default parameters.
detector = cv2.SimpleBlobDetector()

if im is None:
    print("No image called \"" + imageName + "\" found.")
else:
    print("Test 1")
    # Detect blobs.
    keypoints = detector.detect(im)

    print("Test 2")
 
    # Draw detected blobs as red circles.
    # cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
    im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
 
    # Show keypoints
    cv2.imshow("Keypoints", im_with_keypoints)
    cv2.waitKey(0)

print("Finished.")
