import cv2 as cv

image = cv.imread("../images/image1.jpg") 
cv.imshow('Window', image)
cv.waitKey(0)
cv.destroyAllWindows()