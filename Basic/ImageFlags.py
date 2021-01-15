import cv2 as cv 

img = cv.imread('../images/RGB.png', cv.IMREAD_GRAYSCALE)
img2 = cv.imread('../images/RGB.png', cv.IMREAD_REDUCED_COLOR_4)

cv.imshow("gray", img)
cv.imshow('img2', img2)
cv.waitKey(0)
cv.destroyAllWindows()



'''	
IMREAD_COLOR
IMREAD_GRAYSCALE
IMREAD_LOAD_GDAL
IMREAD_ANYCOLOR
# Reading Reduce Size image 
------------------------
IMREAD_REDUCED_COLOR_2
IMREAD_REDUCED_COLOR_4
IMREAD_REDUCED_COLOR_8
IMREAD_REDUCED_GRAYSCALE_2
IMREAD_REDUCED_GRAYSCALE_4
IMREAD_REDUCED_GRAYSCALE_8
--------------------------
Reading with No changes 
IMREAD_UNCHANGED
'''