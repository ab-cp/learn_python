import numpy as np
import torch
import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np

'''
t = np.linspace(0, 40, 100) # start, finish, n points
d_r = 2.5 * t 
d_s = 3 * (t-5)
fig, ax = plt.subplots()
plt.title('A Bank Robber Caught')
plt.xlabel('time (in minutes)')
plt.ylabel('distance (in km)')
ax.set_xlim([0, 40])
ax.set_ylim([0, 100])
ax.plot(t, d_r, c='green')
ax.plot(t, d_s, c='brown')
plt.axvline(x=30, color='red', linestyle='--')
_ = plt.axhline(y=75, color='purple', linestyle='--')

plt.show()
'''


X = np.array([[1, 2], [3, 4]])
'''
array([[1, 2],
       [3, 4]])

browsing a matric in python 
    sum=0.0
    for row in X:
        #print(row)
        for y in row:
            sum += y**2
    print(sum**(1/2))
'''

val = np.linalg.norm(X) 
# 5.477225575051661
print("(1**2 + 2**2 + 3**2 + 4**2)**(1/2) = ", val)

X_pt = torch.tensor([[1, 2], [3, 4.]]) # torch.norm() supports floats only
print(torch.norm(X_pt))

X_tf = tf.Variable([[1, 2], [3, 4.]]) # torch.norm() supports floats only
print(tf.norm(X_tf))


