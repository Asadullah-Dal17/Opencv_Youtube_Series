#Video Recording Script
import cv2 as cv 

cap = cv.VideoCapture('carVideo.mp4')
width = cap.get(cv.CAP_PROP_FRAME_WIDTH)/3
height = cap.get(cv.CAP_PROP_FRAME_HEIGHT)/3
FPS = cap.get(cv.CAP_PROP_FPS)

# video recording paramters 
fourcc = cv.VideoWriter_fourcc(*'XVID')
Recoder = cv.VideoWriter('false.avi', fourcc, FPS,(int(width), int(height))) # keep the same size, of resize and video recorder 

while True:
    ret, frame = cap.read()
    if ret is False:
        break
    # cv.imshow('frame', frame)
    resized = cv.resize(frame, (int(width), int(height)), interpolation=cv.INTER_AREA)
    Recoder.write(resized)

    key = cv.waitKey(1)
    if key ==ord('q'):
        break
cv.destroyAllWindows()
Recoder.release()
cap.release()
print('done')