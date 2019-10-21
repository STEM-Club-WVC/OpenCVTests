import cv2  
  
# path  
path = r'C:\Users\Rajnish\Desktop\geeksforgeeks.png'
  
# Reading an image in default mode 
image = cv2.imread(r'D:\C# Projects\Git\OpenCVTests\Line Detection\src.jpg') 
  
# Window name in which image is displayed 
window_name = 'image'
  
# Using cv2.imshow() method  
# Displaying the image  
cv2.imshow(window_name, image)  
