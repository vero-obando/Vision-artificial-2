# Cambiar el color de fondo de una imagen
import cv2 as cv
import numpy as np

img = cv.imread('cat.jpg')
imgB = cv.imread('cat.jpg',0)
height, width = img.shape[:2]  
img2 = np.zeros((height, width, 3), np.uint8)

img2[:] = (255,0,0)

_, thresh1 = cv.threshold(imgB, 100, 255, cv.THRESH_BINARY_INV)
_, thresh2 = cv.threshold(imgB, 100, 255, cv.THRESH_BINARY)

gato = cv.bitwise_and(img, img, mask=thresh1)
fondo= cv.bitwise_and(img2, img2, mask= thresh2)
res = cv.addWeighted(gato, 1,fondo, 1,0)


cv.imshow('Original', img) 
cv.imshow('Cambio de fondo',res)  
cv.waitKey(0)
cv.destroyAllWindows()