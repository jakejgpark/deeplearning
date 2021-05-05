import numpy as np
import matplotlib.pyplot as plt

#입력층 1
X=np.array([1.0, 0.5])
W1=np.array([[0.1, 0.3, 0.5],[0.2,0.4,0.6]])
B1=np.array([0.1,0.2,0.3])

def sigmoid(x):
    y=1/(np.exp(-x)+1)
    return y

# 은닉층 1
A1=np.dot(X, W1)+B1
Z1=sigmoid(A1)
print(Z1)

# 은닉층 2
W2=np.array([[0.1,0.4],[0.2,0.5],[0.3,0.6]])
B2=np.array([0.1,0.2])

A2=np.dot(Z1,W2)+B2
Z2=sigmoid(A2)
print(Z2)


#출력층
def identify_function(x):
    return x

W3=np.array([[0.1,0.3],[0.2,0.4]])
B3=np.array([0.1,0.2])

A3=np.dot(Z2,W3)+B3

Y=identify_function(A3)
print(Y)


