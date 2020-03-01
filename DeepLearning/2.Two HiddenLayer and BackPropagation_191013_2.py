import numpy as np
import matplotlib.pyplot as plt

lr = 0.7
iteration = 5000

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

X = np.array([[0.00], [0.10], [0.20], [0.30], [0.40], [0.50], [0.60], [0.70], [0.80], [0.90], [1.00]])
Y = np.array([0.00, 0.36, 0.64, 0.84, 0.96, 1.00, 0.96, 0.84, 0.64, 0.36, 0.00])

W = np.random.rand(11, 4)
b_W = np.random.rand(1, 4)
V = np.random.rand(4, 11)
b_V = np.random.rand(1, 11)

for i in range(iteration):
    net1 = np.dot(X.T, W) + b_W
    h1 = sigmoid(net1)
    net2 = np.dot(h1, V) + b_V
    h2 = sigmoid(net2)
    o2 = h2

    dE_db_V = (Y - o2) * o2 * (1 - o2)
    sum_dE_db_V = -np.sum(dE_db_V, axis=0, keepdims=True)
    sum_dE_dV = np.dot(-h1.T, dE_db_V)
    dE_db_W = np.dot(dE_db_V, V.T) * h1 * (1 - h1)
    sum_dE_db_W = -np.sum(dE_db_W, axis=0, keepdims=True)
    sum_dE_dW = -np.dot(X, dE_db_W)

    V = V - sum_dE_dV * lr
    b_V = b_V - sum_dE_db_V * lr
    W = W - sum_dE_dW * lr
    b_W = b_W - sum_dE_db_W * lr

    if i == 0:
        print("==net1===================")
        print(np.round(net1, 3))
        print("==h1=====================")
        print(np.round(h1, 3))
        print("==net2===================")
        print(np.round(net2, 3))
        print("==o2=====================")
        print(np.round(o2, 3))
        print("==dE/dVbais==================")
        print(np.round(-dE_db_V, 4))
        print("==sum(dE/dV)==================")
        print(np.round(sum_dE_dV, 4))
        print("==sum(dE/dVbais)============")
        print(np.round(sum_dE_db_V, 4))
        print("==dE/dWbais==================")
        print(np.round(-dE_db_W, 4))
        print("==sum(dE/dW)==================")
        print(np.round(sum_dE_dW, 4))
        print("==sum(dE/dWbais)============")
        print(np.round(sum_dE_db_W, 4))
        print("============================")

    if i % 500 == 0:
        print("%d번째 o2는 :" % i, *np.round(o2, 4))