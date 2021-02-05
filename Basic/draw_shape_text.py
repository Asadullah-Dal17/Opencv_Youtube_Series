import cv2 as cv 
import numpy as np 

"""create empty image """
image = np.zeros((480, 640, 3), dtype=np.uint8)
x, y = 100, 50 # Postion on the image Column and Row (x,y)
h, w = 100, 200 # height and Width of Rectangle 
yellow= (0,255,255) # Colors (Blue, Green, Red)

RADIUS= 30 # Radius of Circle 

FONTS =cv.FONT_HERSHEY_COMPLEX 
""" create Rectangle """
# cv.rectangle(img=image, pt1=(x,y), pt2=(x + w, y + h), color=yellow, thickness=-1)
""" creating Circle here """
# cv.circle(img=image, center =(x,y), radius=RADIUS, color=yellow, thickness=2)
""" Drwaing Text here """
# cv.putText(img= image, text= "AI Phile", org=(x,y), fontFace=FONTS, fontScale=1.6, color=yellow, thickness=2 )

points = np.array([[20,100], [70, 130], [170, 160], [200,400]], np.int32)
""" reshaping the array """
points= points.reshape((-1,1,2))

""" draw the polylines """
cv.polylines(img=image, pts=[points], isClosed=False, color=yellow, thickness=3)

""" Dipalye the image on the screen """
cv.imshow("image ", image)
cv.waitKey(0)
cv.destroyAllWindows()