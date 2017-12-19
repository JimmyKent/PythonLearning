# import matplotlib.pyplot as plt
# from pylab import *
# import time
#
# X = []
# Y = []
# plt.ion()
# for i in range(5):
#     X.append(i)
#     Y.append(Y)
#     plt.scatter(X, Y)
#     plt.pause(1)
#     show()
#
# while True:
#     plt.pause(0.05)

# https://codeday.me/bug/20170625/32749.html
import numpy as np
import matplotlib.pyplot as plt

plt.axis([0, 10, 0, 1])

for i in range(10):
    y = np.random.random()
    plt.scatter(i, y)
    plt.pause(0.5)
plt.show()
# print(y)

