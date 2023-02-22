"""
Regresion lineal Punto de partida
"""

"""
Punto de partida
"""

import numpy as np
import matplotlib.pyplot as plt


LR = 0.00005
EPOCHS = 20



dataset = np.loadtxt('train.csv', delimiter=";")
X = dataset[:,0,None] # Preservar la dimensión y que quede como un vector, 
y = dataset[:,1,None]

# Estandarizar datos

X = (X - np.mean(X))/np.std(X) 
y = (y - np.mean(y))/np.std(y) 

# Agregar columna de 1 a X para multiplicar por theta_0
m = X.shape[0]
X_0 = np.ones((m,1))
X = np.hstack((X_0,X))

# Parámetros a optimizar
theta = np.random.rand(2)
print(theta)

# print (X)

for i in range (EPOCHS):

    y_predicted = X @ theta # y gorrito

    err = y_predicted - y
    # print(err)

    err_sum = 1/m * np.sum(err) # dJ/dtetha_0 = Eerr
    # print(err_sum)

    err_sum_X = 1/m * (np.sum(err* X[:,1,None])) # dJ/dtetha_1 = EerrX 

    theta[0] = theta[0] - LR * err_sum
    theta[1] = theta[1] - LR * err_sum_X

    print (f"Tetha_0: {theta[0]}")
    print (f"Tetha_1: {theta[1]}")
    print("-"*50)


    prediction = theta[0] + theta[1]*X[:,1]

    plt.plot(X[:,1], prediction, 'r')

plt.scatter(X[:,1],y)

plt.show()