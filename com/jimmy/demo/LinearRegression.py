import numpy as np


def load_data(filename):
    """
    Returns:
    X : 1
    y : 价格

    """
    num_feat = len(open(filename).readline().split('\t')) - 1
    X = []
    y = []
    file = open(filename)
    for line in file.readlines():
        line_arr = []
        cur_line = line.strip().split("\t")
        for i in range(num_feat):
            line_arr.append(float(cur_line[i]))
        line_arr.insert(0, float(1))
        X.append(line_arr)
        y.append(float(cur_line[-1]))
    return np.mat(X), np.mat(y).T


if __name__ == "__main__":
    X, y = load_data('houses.txt')  # 只有一个变量x, 才是一元方程,才是在平面的图像
