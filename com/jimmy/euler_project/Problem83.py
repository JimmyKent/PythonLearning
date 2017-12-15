# 从左上角走到右下角 425185

import numpy as np
from heapq import *
import sys


def read_data(filename, split):
    line_length = len(open(filename).readline().split(split))
    matrix_x = []

    file = open(filename)
    for line in file.readlines():
        line_arr = []
        cur_line = line.strip().split(split)
        for i in range(line_length):
            line_arr.append(float(cur_line[i]))
        matrix_x.append(line_arr)

    return np.mat(matrix_x)


class Node:
    x = 0
    y = 0
    distance = 0

    def __eq__(self, other):
        return self.x * 100 + self.y == other.x * 100 + other.y

    def __lt__(self, other):  # operator <
        return self.x * 100 + self.y < other.x * 100 + other.y

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ", " + str(self.distance) + ")"


original = read_data("p81-82-83_matrix.txt", ',')

DEFAULT_DISTANCE = 100000000
print(sys.maxsize / 2)

disMatrix = np.copy(original)

print(disMatrix)

# 获得矩阵的行数
# for i in range(1, Y.shape[0]):
#     Y[i, 0] += Y[i - 1, 0]
#
# for j in range(1, Y.shape[1]):
#     Y[0, j] += Y[0, j - 1]
#
# for x in range(1, Y.shape[0]):
#     for y in range(1, Y.shape[1]):
#         Y[x, y] += min(Y[x - 1, y], Y[x, y - 1])
#
# print(Y)
# print(Y[79, 79])

#
# node1 = Node()
# node1.x = 2
# node2 = Node()
# node2.x = 3
# print(node1 == node2)
#
# nodes = []
# nodes.append(node1)
# nodes.append(node2)
# heapify(nodes)
# test = heappop(nodes)
# print(test)
# test2 = heappop(nodes)
# print(test2)
