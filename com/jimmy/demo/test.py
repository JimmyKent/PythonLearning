import numpy as np
import random
import matplotlib.pyplot as plt


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
        loss = hwx - y  # 公式里的括号项
        cost = np.sum(loss ** 2) / (2 * m)  # 代价函数, 方差
        # print("Iteration %d | Cost: %f " % (i, cost))
        gradient = np.dot(xTrans, loss) / m  # 更新梯度
        theta = theta - alpha * gradient  # 同时更新theta0, theta1
    return theta


def genData(numPoints, bias, variance):
    """
    generation data
    :param numPoints: 生成点的个数
    :param bias: 偏移值
    :param variance: 波动值,误差,方差
    :return: x 是一个 一维特征, 因为 y = ax + b; 中的b存在,构造y = ax1 + bx0;
    所有x会构建成[[1,0] [1, 2] ...] 的形式, 相当于 x0, x1 两个特征, x0永远为1, x1 递增

    """
    x = np.zeros(shape=(numPoints, 2))
    y = np.zeros(shape=numPoints)
    for i in range(0, numPoints):
        x[i][0] = 1
        x[i][1] = i
        y[i] = (i + bias) + random.uniform(0, 1) * variance
    return x, y


def plotData(x, y, theta):
    plt.scatter(x[..., 1], y)
    plt.plot(x[..., 1], [theta[0] + theta[1] * xi for xi in x[..., 1]])
    plt.show()


if __name__ == "__main__":
    x, y = genData(20, 25, 10)
    print(x)
    print("------")
    print(y)
    iterations = 10000
    alpha = 0.001
    theta = gradientDescent(x, y, alpha, iterations)
    plotData(x, y, theta)
