import cv2 as cv 

def helper(x):
    pass
cv.namedWindow('windows')
cv.createTrackbar('Hue', 'windows', 0,100, helper)
cv.createTrackbar('Brightness', 'windows', 0, 100, helper)


cap = cv.VideoCapture(1)
width = cap.get(cv.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv.CAP_PROP_FRAME_HEIGHT)
fps = cap.get(5)
print(fps, 'w', width, 'h', height  )
cap.set(3, int(width/3))
cap.set(4, int(height/4))
while True:
    ret, frame = cap.read()
    if ret is False:
        break
    hue = cv.getTrackbarPos('Hue', 'windows')
    brightness = cv.getTrackbarPos('Brightness', 'windows')
    cap.set(10, brightness)
    cap.set(13, hue)
    
    cv.imshow('window', frame)

    key = cv.waitKey(1)
    if key == ord('q'):
        break
cv.destroyAllWindows()
cap.release()
