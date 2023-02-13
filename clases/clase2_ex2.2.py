# Implementar operadores de punto y realizar un ejemplo

import cv2 as cv
import numpy as np
# Brillo y contraste 

im = cv.imread('test_im.jpg')



# Mezcla lineal

im2 = cv.imread('day.jpg')
im3 = cv.imread('night.jpg')
res = cv.addWeighted(im2, 0.5 ,im3, 0.5 ,0)

cv.imshow('Mezcla lineal',res)
cv.waitKey(0)
cv.destroyAllWindows()

#Correccion gamma

height, width = im.shape[:2]  # Obtenemos sus dimensiones
imgGamma = np.zeros((height, width, 3), np.uint8)  # Creamos una imagen nueva
invGamma = 1/2  # Se define el valor de Gamma
for i in range(0, width):
    for j in range(0, height):
        imgGamma[j] = 255*((im[j]/255.0) ** invGamma)  # Ecucacion de correccion Gamma

cv.imshow('Correccion gamma', np.hstack([im, imgGamma]))  # Mostramos las imagenes
cv.waitKey(0)
cv.destroyAllWindows()

# Image matting
sky = cv.imread('sky.jpg')
mask = cv.imread('test_im-A.jpg',0)

_, thresh1 = cv.threshold(mask, 100, 255, cv.THRESH_BINARY_INV)

gato = cv.bitwise_and(im, im, mask=mask)
fondo= cv.bitwise_and(sky, sky, mask= thresh1)
resl = cv.addWeighted(gato, 1,fondo, 1,0)

cv.imshow('Original', im) 
cv.imshow('Cambio de fondo',resl)   
cv.waitKey(0)
cv.destroyAllWindows()

