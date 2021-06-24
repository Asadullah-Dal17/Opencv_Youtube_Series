import cv2 as cv 

cap = cv.VideoCapture('carVideo.mp4')

while True:
    ret, frame = cap.read()
    if ret is False:
        break
    cv.imshow('frame', frame)

    key = cv.waitKey(1)
    if key ==ord('q'):
        break
cv.destroyAllWindows()
cap.release()