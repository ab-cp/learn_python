import numpy as np

Y = np.matrix('1 2; 3 4')
X = np.matrix('1 2; 3 4 ; 5 ,6') 
print("X=", X)
print(X.ndim)
dimensionsX = np.shape(X)
rowsX, columnsX = dimensionsX
print("X dimensitons = ",  dimensionsX)

print("Y=",Y)
print(Y.ndim)
dimensionsY = np.shape(Y)
rowsY, columnsY = dimensionsY
print("Y dimensitons = ", dimensionsY)

if(columnsX == rowsY):
    print("X*Y\n-------")
    print(X*Y)
    print("-------")
else:
    print("incorrect dimensions for X {}, Y {}".format(dimensionsX, dimensionsY))
if(columnsY == rowsX):
    print(Y*X)
else:
    print("incorrect dimensions for X {}, Y {}".format(dimensionsX, dimensionsY))
    
