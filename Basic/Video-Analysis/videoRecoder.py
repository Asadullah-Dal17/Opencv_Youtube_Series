import cv2 as cv 

cap = cv.VideoCapture(0)
width = cap.get(cv.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv.CAP_PROP_FRAME_HEIGHT)
fps = cap.get(5)
print(fps, 'w', width, 'h', height  )

fourcc = cv.VideoWriter_fourcc(*'XVID')
Recoder = cv.VideoWriter('output_changed.mp4', fourcc, fps, (int(width/2), int(height/2)))
while True:
    ret, frame = cap.read()
    if ret is False:
        break
    resize = cv.resize(frame, (int(width/2), int(height/2)), interpolation= cv.INTER_AREA)
    cv.imshow('window', frame)
    Recoder.write(resize)

    key = cv.waitKey(1)
    if key == ord('q'):
        break
cv.destroyAllWindows()
Recoder.release()
cap.release()
