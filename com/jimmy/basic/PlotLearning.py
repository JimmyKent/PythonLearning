import numpy as np
import matplotlib.pyplot as plt


def draw_point(x_list, y_list):
    # 绘制散列点
    plt.plot(x_list, y_list, '*')
    plt.show()


def draw_line(a, b):
    """
    关键在于
    1.坐标轴的取值范围
    2.x的取值范围
    y = ax + b
    :param a:
    :param b:

    """
    plt.figure()  # 实例化作图变量
    plt.title('line')  # 图像标题
    plt.xlabel('x')  # x轴文本
    plt.ylabel('y')  # y轴文本
    plt.grid(True)  # 是否绘制网格线
    x = np.linspace(0, 50, 10)  # 在0-5之间生成10个点的向量
    print("x", x)
    plt.plot(x, a * x + b, 'g-')  # 绘制y=2x图像，颜色green，形式为线条
    plt.show()  # 展示图像


def draw_line_range(a, b, x_y_range):
    """
    关键在于
    1.坐标轴的取值范围
    2.x的取值范围
    y = ax + b
    :param a:
    :param b:
    :param x_y_range: x, y轴的范围. eg: [0, 5, 0, 10]  # x轴范围0-5，y轴范围0-10
    """
    plt.figure()  # 实例化作图变量
    plt.title('line')  # 图像标题
    plt.xlabel('x')  # x轴文本
    plt.ylabel('y')  # y轴文本
    plt.axis(x_y_range)  # x轴范围，y轴范围
    plt.grid(True)  # 是否绘制网格线
    x = np.linspace(x_y_range[0], x_y_range[1], 10)  # 在x之间生成10个点的向量
    print("x", x)
    plt.plot(x, a * x + b, 'r-')  # 绘制y=2x图像，颜色green，形式为线条
    plt.show()  # 展示图像


if __name__ == "__main__":
    draw_line(1, 1)

    draw_line_range(10, 10, [-10, 50, -10, 600])
