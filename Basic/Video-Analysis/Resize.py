import cv2 as cv 
def helper(x):
    pass
cv.namedWindow('frame')
cv.createTrackbar('Brightness','frame', 0,100, helper)
cv.createTrackbar('hue', 'frame', 0,100, helper)
cap = cv.VideoCapture(1)
height = cap.get(cv.CAP_PROP_FRAME_HEIGHT)
width = cap.get(cv.CAP_PROP_FRAME_WIDTH)
fps = cap.get(cv.CAP_PROP_FPS)
print(width, height, "fps : ", fps)
# cap.set(cv.CAP_PROP_FRAME_WIDTH, int(width))
# cap.set(cv.CAP_PROP_FRAME_HEIGHT, int(height))


while True:
    ret, frame = cap.read()
    if ret is False:
        break
    brightness = cv.getTrackbarPos('Brightness', 'frame')
    hue = cv.getTrackbarPos('hue', 'frame')
    cap.set(10, brightness)
    cap.set(13, hue)
    # resize = cv.resize(frame, (int(width/3), int(height/3)), interpolation=cv.INTER_AREA)
    # cv.imshow('resize', resize)
    cv.imshow('frame', frame)

    key = cv.waitKey(1)
    if key ==ord('q'):
        break
cv.destroyAllWindows()
cap.release()