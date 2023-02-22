# Ejercicios de clase introduccion

import cv2 as cv 
import numpy as np 
import math
s = 100

def im_1():
    im =np.zeros([100,100]) 
    for i in range (s):
        im[i,i] = 255
    
    cv.imwrite('imagen1.jpg', im)

im_1()

def im_2():
    im2= np.zeros([100,100,3],np.uint8)
    rect1 = cv.rectangle(im2, (35,35), (65,65), (0,0,255),-1)
    rect2 = cv.rectangle(rect1, (40,40), (60,60), (0,255,0),-1)
    rect3 = cv.rectangle(rect2, (45,45), (55,55), (255,0,0),-1)
    rect4 = cv.rectangle(rect3, (48,48), (52,52), (0,0,0),-1)

    cv.imwrite('imagen2.jpg',rect4)

im_2()

def im_3():
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


    cv.imwrite('imagen3.jpg', img)

im_3()



