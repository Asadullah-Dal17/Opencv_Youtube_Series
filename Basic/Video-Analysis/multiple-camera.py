import cv2 as cv 

cap = cv.VideoCapture(0)
cap1 =cv.VideoCapture(3)

while True:
    ret, frame = cap.read()
    ret1, frame1 = cap1.read()
    if ret is False:
        break
    frame1 = cv.cvtColor(frame1, cv.COLOR_BGR2GRAY)

    cv.imshow('window', frame)
    cv.imshow('window1', frame1)

    key = cv.waitKey(1)
    if key == ord('q'):
        break
cv.destroyAllWindows()
cap.release()
