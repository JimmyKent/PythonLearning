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


def load_data2(filename):
    """
    Matrix.T : T -- transpose 转置
    Matrix.I : I -- inverse 逆运算
    Returns:
    X : 1
    y : 价格

    """
    num_feat = len(open(filename).readline().split('\t')) - 1
    X = []
    file = open(filename)
    for line in file.readlines():
        line_arr = 0
        cur_line = line.strip().split("\t")
        for i in range(num_feat):
            line_arr = int(cur_line[i])
        # line_arr.insert(0, float(1))
        X.append(line_arr)
    return X


if __name__ == "__main__":
    X, y = load_data('houses.txt')  # 只有一个变量x, 才是一元方程,才是在平面的图像

    X_O = load_data2('houses.txt')

    print(X_O)

    print("----------------")

    print(y)

    print("----------------")

    X_T = np.transpose(X)
    X_T_X = X_T * X
    X_T_X_I = X_T_X.I
    theta = X_T_X_I * X_T * y

    print(theta)
    print(X_O)

    a = theta[0][0]
    b = theta[1][0]

    print(a, b)

    # 绘制散列点
    plt.plot(X_O, y, '*')
    # 绘制拟合曲线
    x = np.linspace(1000, 5000, 2)  # 在0-5之间生成10个点的向量
    plt.plot(x, 71270.49244873 + 134.52528772 * x, 'g-')  # 绘制y=2x图像，颜色green，形式为线条

    plt.show()

    # plt.figure()  # 实例化作图变量
    # plt.title('single variable')  # 图像标题
    # plt.xlabel('x')  # x轴文本
    # plt.ylabel('y')  # y轴文本
    # #plt.axis([0, 5, 0, 10])  # x轴范围0-5，y轴范围0-10
    # plt.grid(True)  # 是否绘制网格线
    # xx = np.linspace(0, 5, 10)  # 在0-5之间生成10个点的向量
    #
    # #print("xx",xx)
    #
    # plt.plot(xx, 71270.49244873 * xx + 134.52528772, 'g-')  # 绘制y=2x图像，颜色green，形式为线条
    # plt.show()  # 展示图像
