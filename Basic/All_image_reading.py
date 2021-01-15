import os 
import cv2 as cv

Dir_img ='..\images'

Files = os.listdir(Dir_img)

for f in Files:
    ImgPath = os.path.join(Dir_img,f)
    print('complete path ', ImgPath)
    image = cv.imread(ImgPath, cv.IMREAD_GRAYSCALE)
    cv.imwrite(f'../results/{f}.png', image)

