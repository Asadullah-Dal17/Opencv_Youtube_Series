import cv2 as cv 


image = cv.imread('../images/RGBA.png', cv.IMREAD_UNCHANGED)
blue, green , red, A = cv.split(image)
cv.imshow('orginal', image)
cv.imshow('blue', blue)
cv.imshow('green', green)
cv.imshow('red', red)
cv.imshow('a',A)
cv.waitKey(0)

cv.destroyAllWindows()