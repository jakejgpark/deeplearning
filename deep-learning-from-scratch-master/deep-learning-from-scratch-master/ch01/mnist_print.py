import sys, os
sys.path.append(os.pardir)
sys.path.append("E:\\coding\\deeplearning\\deep-learning-from-scratch-master\\deep-learning-from-scratch-master")

import numpy as np
from dataset.mnist import load_mnist

np.set_printoptions(linewidth=200, threshold=1000)
(x_train, t_train),(x_test,t_test)=load_mnist(flatten=False, normalize=False)

print(x_train[0])
