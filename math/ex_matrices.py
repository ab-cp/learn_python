import numpy as np
import tensorflow as tf
import torch

#print(torch.tensor([[1,2],[3,4]]))

U  = np.array([[2],[5],[3]])
I  = np.identity(3)
UI = np.multiply(U,I)
print(UI)

#UI = np.matmul(U,I)
#print(UI)


