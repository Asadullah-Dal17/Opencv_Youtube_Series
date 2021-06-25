import cv2 as cv 

cap = cv.VideoCapture(0)
cap2 = cv.VideoCapture(3)

while True:
    ret, frame = cap.read()
    ret, frame1 = cap2.read()
    if ret is False:
        break
    gray =cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow('frame', gray)
    cv.imshow('frame1', frame1)


    key = cv.waitKey(1)
    if key ==ord('q'):
        break
cv.destroyAllWindows()
cap.release()