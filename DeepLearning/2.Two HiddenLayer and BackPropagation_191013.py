import numpy as np
import matplotlib.pyplot as plt

lr = 0.5
iteration = 100000


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


X = np.array([[1, 1], [1, 0], [0, 1], [0, 0]])
Y = np.array([[0], [1], [1], [0]])

W = np.array([[-0.089, 0.098], [0.028, -0.07]])
b_W = np.array([[0.092, -0.01]])
V = np.array([[0.056], [0.067]])
b_V = np.array([[0.016]])

for i in range(iteration):
    net1 = np.dot(X, W) + b_W
    h1 = sigmoid(net1)
    net2 = np.dot(h1, V) + b_V
    h2 = sigmoid(net2)
    o2 = h2

    dE_db_V = (Y - o2) * o2 * (1 - o2)
    sum_dE_db_V = -np.sum(dE_db_V, axis=0, keepdims=True)
    dE_dV = -h1 * dE_db_V
    sum_dE_dV = np.dot(-h1.T, dE_db_V)
    dE_db_W = np.dot(dE_db_V, V.T) * h1 * (1 - h1)
    sum_dE_db_W = -np.sum(dE_db_W, axis=0, keepdims=True)
    dE_dW = -X * dE_db_W
    sum_dE_dW = -np.dot(X.T, dE_db_W)

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
        print("==dE/dV==================")
        print(np.round(dE_dV, 4))
        print("==dE/dVbais==================")
        print(np.round(-dE_db_V, 4))
        print("==sum(dE/dV)==================")
        print(np.round(sum_dE_dV, 4))
        print("==sum(dE/dVbais)============")
        print(np.round(sum_dE_db_V, 4))
        print("==dE/dW============")
        print(np.round(dE_dW, 4))
        print("==dE/dWbais==================")
        print(np.round(-dE_db_W, 4))
        print("==sum(dE/dW)==================")
        print(np.round(sum_dE_dW, 4))
        print("==sum(dE/dWbais)============")
        print(np.round(sum_dE_db_W, 4))
        print("============================")

    if i % 1000 == 0:
        print("%d번째 o2는 :" % i, *np.round(o2, 4))