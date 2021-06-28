import cv2 as cv 

cap = cv.VideoCapture('Video.mp4')

while True:
    ret, frame = cap.read()
    if ret is False:
        break

    cv.imshow('window', frame)

    key = cv.waitKey(1)
    if key == ord('q'):
        break
cv.destroyAllWindows()
cap.release()
