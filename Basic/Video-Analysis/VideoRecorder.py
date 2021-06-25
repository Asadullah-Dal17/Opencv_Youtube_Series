#Video Recording Script
import cv2 as cv 

cap = cv.VideoCapture('carVideo.mp4')
width = cap.get(cv.CAP_PROP_FRAME_WIDTH)

height 

# video recording settings 
fourcc = cv.VideoWriter_fourcc(*'XVID')
Recorder = cv.VideoWriter('outputVideo.avi', fourcc, fps, (width, height))

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