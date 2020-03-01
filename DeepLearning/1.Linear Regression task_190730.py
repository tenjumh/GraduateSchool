#데이타 = [(0.0, 0.0), (1.0, 1.0), (1.0, 2.0), (2.0, 1.0)]
#Approximater -> f(x; w0, w1, w2) = w2*x^2 + w1*x + w0
#learning_rate = 0.05
#w0, w1, w2는 random하게 초기화
import numpy as np

x = [0.0, 1.0, 1.0, 2.0]
y = [0.0, 1.0, 2.0, 1.0]
w = [np.random.rand(), np.random.rand(), np.random.rand()]
lr = 0.005
for i in range(5000):
    gw0, gw1, gw2 = 0, 0, 0
    for j in range(len(x)):
        fx = w[2] * x[j] ** 2 + w[1] * x[j] + w[0]
        gw0 += -2 * (y[j] - fx)
        gw1 += -2 * (y[j] - fx) * x[j]
        gw2 += -2 * (y[j] - fx) * x[j] ** 2
        # print(gw0, gw1, gw2)
    if i % 100 == 0:
        print("{}회, w0 : {}, w1 : {}, w2 : {}".format(i + 1, w[0], w[1], w[2]))
    w[0] = w[0] - lr * gw0
    w[1] = w[1] - lr * gw1
    w[2] = w[2] - lr * gw2

print("모델모형은 : f(x) = {}x^2 + {}x + {}".format("%.3f" % w[2], "%.3f" % w[1], "%.3f" % w[0]))
