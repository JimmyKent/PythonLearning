# 从左上角走到右下角

import numpy as np


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


Y = read_data("p81-82-83_matrix.txt", ',')

# 获得矩阵的行数
for i in range(1, Y.shape[0]):
    Y[i, 0] += Y[i - 1, 0]

for j in range(1, Y.shape[1]):
    Y[0, j] += Y[0, j - 1]

for x in range(1, Y.shape[0]):
    for y in range(1, Y.shape[1]):
        Y[x, y] += min(Y[x - 1, y], Y[x, y - 1])

print(Y)
print(Y[79, 79])
