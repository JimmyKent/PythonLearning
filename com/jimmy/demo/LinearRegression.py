import numpy as np
import matplotlib.pyplot as plt


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


def gradientDescent(x, y, alpha, numIterations):
    """
    这部分要结合公式看

    :param x:
    :param y:
    :param alpha: 步长
    :param numIterations:
    :return:
    """
    xTrans = x.transpose()  # transpose 转置 相当于x.T
    m, n = np.shape(x)  # shape 返回x的形状，m = 20, n = 2; 20行2列
    theta = np.ones(n)  # 用1填充n形状（矩阵）
    for i in range(0, numIterations):  # 迭代一万次
        hwx = np.dot(x, theta)  # hypothesis 猜测函数
        loss = hwx - y  # 公式里的括号项, loss equals J(theta)
        cost = np.sum(loss ** 2) / (2 * m)  # 代价函数 方差
        # print("Iteration %d | Cost: %f " % (i, cost))
        gradient = np.dot(xTrans, loss) / m  # 更新梯度
        theta = theta - alpha * gradient  # 同时更新theta0, theta1
    return theta


def plotData(x, y, theta):
    plt.scatter(x[..., 1], y)
    plt.plot(x[..., 1], [theta[0] + theta[1] * xi for xi in x[..., 1]])
    plt.show()


if __name__ == "__main__":
    X, y = load_data('houses20.txt')  # 只有一个变量x, 才是一元方程,才是在平面的图像
    print(X)
    print("------")
    print(y)
    iterations = 10000
    alpha = 0.001
    theta = gradientDescent(X, y, alpha, iterations)
    plotData(X, y, theta)
