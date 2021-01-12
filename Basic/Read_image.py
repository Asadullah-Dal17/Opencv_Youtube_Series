# loading in the module opencv
import cv2 as cv
# reading image from directory
image = cv.imread("../images/image1.jpg")
# Display the image using imshow function  
cv.imshow('Window', image)
# making opencv for wait until we press any key on the keyboard 
cv.waitKey(0)
# Closing all the windows 
cv.destroyAllWindows()