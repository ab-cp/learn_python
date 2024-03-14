#!python
import numpy as np
import matplotlib.pyplot as plt

A = np.zeros(10)
B = np.zeros((3,4))
a = np.zeros((3,4))
print(a)
print("a.ndim={}\r\na.size={}".format(a.ndim,a.size))

print("np.zeros((2,3,4))")
print(np.zeros((2,3,4)))

print("type(np.zeros((3,4)))")
print(type(np.zeros((3,4))))

print("np.ones((3,4))")
print(np.ones((3,4)))

A=np.array([[1,2,3,4], [10, 20, 30, 40]])
print(A)


plt.hist(np.random.rand(100000), density=True, bins=100, histtype="step", color="blue", label="rand")
plt.hist(np.random.randn(100000), density=True, bins=100, histtype="step", color="red", label="randn")
plt.axis([-2.5, 2.5, 0, 1.1])
plt.legend(loc = "upper left")
plt.title("Random distributions")
plt.xlabel("Value")
plt.ylabel("Density")
plt.show()