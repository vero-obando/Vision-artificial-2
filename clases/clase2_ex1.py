# Transformaciones geometricas

import numpy as np
import cv2 as cv

W = 500
H = 500

im = np.zeros([W,H,3])

def show_im (im):
    cv.imshow('window', im)
    cv.waitKey(0)

def draw (triangle, im, color = (0,255,0)):
    cv.drawContours(im, [triangle.astype(int)],0,color,-1)

def traslate (triangle, dx, dy):
    t = np.array([dx,dy])  # Matriz de traslacion
    return triangle + t

def escalar (triangle, sx, sy):
    e = np.array([sx,sy])
    return triangle*e

def rotar (triangle, angulo):
    r = np.array([[np.cos(angulo),-np.sin(angulo)], [np.sin(angulo), np.cos(angulo)]])
    return triangle @ r

im = np.zeros([W,H,3])
tr = np.array([[10,10], [70,10], [40,60]])  # Vertices del triangulo

draw(tr,im)

# Traslacion
t1 = traslate(tr, 50,50)
draw(t1, im, color= (0,0,255))

# Escalar
e1 = escalar(tr,5,5)
draw(e1,im, color=(255,0,0))

# Rotar
r1 = rotar(tr,90)
draw(r1,im,color=(0,0,255))
show_im(im)