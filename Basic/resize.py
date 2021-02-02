import cv2 as cv 

image = cv.imread("../images/image1.jpg")

# Resized_image = cv.resize(image, None, fx=1.5, fy=1.5)
height = image.shape[0]
width = image.shape[1]

h = int(height*1.5)
w = int(width*1.5)

Resized_image = cv.resize(image, (h, w), interpolation=cv.INTER_AREA)

cv.imshow("image", image)
cv.imshow("resized", Resized_image)

cv.waitKey(0)
cv.destroyAllWindows()