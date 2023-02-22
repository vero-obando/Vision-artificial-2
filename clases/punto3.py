
import numpy as np
import math
import cv2 as cv

width = 500
height = 500

img = np.zeros((height, width), dtype=np.uint8)

amplitude = 10
frequency = 5
phase = 0

for x in range(width):
    # for i in range(10):
    aumento = np.arange(0,480,20)
    for i in range(len(aumento)):
        y = int(amplitude * math.sin(2*math.pi*frequency*x/width + phase)+11+aumento[i])
        img[y, x] = 255


cv.imshow('imagen 3', img)  
cv.waitKey(0) 
cv.destroyAllWindows()
