import numpy as np 
import cv2 as cv 


def nothing(x):
    pass 

cv.namedWindow('image')

cv.createTrackbar('RED', 'image',0, 255, nothing)
cv.createTrackbar('GREEN', 'image',0, 255, nothing)
cv.createTrackbar('BLUE', 'image',0, 255, nothing)
cv.createTrackbar('HEIGHT', 'image',0, 700, nothing)
cv.createTrackbar('WIDTH', 'image',0, 600, nothing)


while True:
    image = np.zeros((600,500,3), dtype=np.uint8)

    red = cv.getTrackbarPos("RED", "image")
    blue = cv.getTrackbarPos("BLUE", "image")
    green = cv.getTrackbarPos("GREEN", "image")
    height = cv.getTrackbarPos("HEIGHT", "image")
    width = cv.getTrackbarPos("WIDTH", "image")

    x =10
    y =10

    cv.rectangle(image, (x,y), (x+width, y +height), (blue, green, red),-1)
    cv.imshow('image', image)
    if cv.waitKey(1)==ord('q'):
        break
cv.destroyAllWindows()
