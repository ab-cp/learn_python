import numpy as np
import tensorflow as tf
import torch

X = np.array([[4, 2], [-5, -3]])
print(X)
'''
[[ 4  2]
 [-5 -3]]
'''

Xinv = np.linalg.inv(X)
print(Xinv)
'''
[[ 1.5  1. ]
 [-2.5 -2. ]]
'''

y = np.array([4, -7])
print(y)
'''
[ 4 -7]
'''

w = np.dot(Xinv, y)
print(w)
'''
[-1.  4.]
'''

# Using pytorch
print("\n-Using Pytorch-")
ans = torch.inverse(torch.tensor([[4, 2], [-5, -3.]])) # float type
print(ans)

# Using tensorflow
print("\n-Using TensorFlow-")
ans = tf.linalg.inv(tf.Variable([[4, 2], [-5, -3.]])) # also float
print(ans)



print("\n")

'''
Matrix Inverse is based on other conditions
- Singular
- Overdetermined and Undetermined system
-- Overdetermined -> # of rows > # of columns
-- UnderDetermined ->  

'''


X = np.array([[-4, 1], [-8, 2]])
print(X)
try:
    print(np.linalg.inv(X))
except:
    print("Inverse not possible")

# Diagonal Matrices
print("Diagonal Matrices")
D1 = np.diag([1,-1,1,-1])
print(D1)
D1_inv = np.linalg.inv(D1)
print(D1_inv)

# Orthogonal Matrices
# A_Trans = A_Inverse
# i.e. matrix multiplied by its Transpose result into identity matrix 
#  e.g.   A * A^T = I



# Trace Operator : Sum of all the elements of diagonal
print("\nTrace example")
A = np.array([[ 25,2], [5,4]])
A_trace = np.trace(A)
print(A_trace)









