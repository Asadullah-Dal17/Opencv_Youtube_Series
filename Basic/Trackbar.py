import numpy as np
import cv2 as cv


def nothing(x):
    pass


cv.namedWindow('Windows')

cv.createTrackbar('RED', 'Windows', 0, 255, nothing)
cv.createTrackbar('GREEN', 'Windows', 0, 255, nothing)
cv.createTrackbar('BLUE', 'Windows', 0, 255, nothing)
cv.createTrackbar('WIDTH', 'Windows', 0, 555, nothing)
cv.createTrackbar('HEIGHT', 'Windows', 0, 490, nothing)

while True:
    frame = np.zeros((600, 600, 3), dtype=np.uint8)

    red = cv.getTrackbarPos('RED', 'Windows')
    blue = cv.getTrackbarPos('BLUE', 'Windows')
    green = cv.getTrackbarPos('GREEN', 'Windows')
    height = cv.getTrackbarPos('HEIGHT', 'Windows')
    width = cv.getTrackbarPos('WIDTH', 'Windows')

    x = 10
    y = 10
    cv.rectangle(frame, (x, y), (x+width, y+height), (blue, green, red), -1)
    cv.imshow('frame', frame)

    key = cv.waitKey(1)
    if key == ord('q'):
        break
cv.destroyAllWindows()
