import os 
import cv2 as cv

DirPath = '..\images'
Files = os.listdir(DirPath)
for File in Files:
    imgPath = os.path.join(DirPath, File)
    print(imgPath)
    image = cv.imread(imgPath, cv.IMREAD_GRAYSCALE)
    cv.imwrite(f'../results/gray_{File}', image)
#     cv.imshow('image', image)
#     cv.waitKey(0)
# cv.destroyAllWindows()

'''	
IMREAD_COLOR
IMREAD_GRAYSCALE
IMREAD_LOAD_GDAL
IMREAD_ANYCOLOR
# Reading Reduce Size image 
------------------------
IMREAD_REDUCED_COLOR_2
IMREAD_REDUCED_COLOR_4
IMREAD_REDUCED_COLOR_8
IMREAD_REDUCED_GRAYSCALE_2
IMREAD_REDUCED_GRAYSCALE_4
IMREAD_REDUCED_GRAYSCALE_8
--------------------------
Reading with No changes 
IMREAD_UNCHANGED
'''