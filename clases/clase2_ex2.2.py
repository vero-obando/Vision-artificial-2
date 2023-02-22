# Implementar operadores de punto y realizar un ejemplo

import cv2 as cv
import numpy as np
# Brillo y contraste 

im = cv.imread('test_im.jpg')/255
a = 1.5
b = 0.2

brillo = (a*im) + b

cv.imshow('Brillo y contraste', brillo)
cv.waitKey(0)
cv.destroyAllWindows()


# Mezcla lineal

im2 = cv.imread('day.jpg')
im3 = cv.imread('night.jpg')
res = cv.addWeighted(im2, 0.5 ,im3, 0.5 ,0)

cv.imshow('Mezcla lineal',res)
cv.waitKey(0)
cv.destroyAllWindows()

#Correccion gamma
y = 2
gamma = im **y

cv.imshow('Correccion gamma',gamma)
cv.waitKey(0)
cv.destroyAllWindows()

# Image matting
sky = cv.imread('sky.jpg')/255
mask = cv.imread('test_im-A.jpg')/255

matting = ((1-mask)*sky) + (mask*im)

cv.imshow('Image matting',matting)
cv.waitKey(0)
cv.destroyAllWindows()



