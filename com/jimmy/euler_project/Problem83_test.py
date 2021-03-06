import numpy as np
from pylab import *
from matplotlib import pyplot as plt

disMatrix = np.loadtxt(
    "/Users/jinguochong/PycharmProjects/PythonLearning/com/jimmy/euler_project/Problem83_distance_matrix.txt",
    delimiter=' ')

print(disMatrix)

DEFAULT_DISTANCE = 100000000


def get_distance(x, y):
    if y < 0 or y >= 80 or x < 0 or x >= 80:
        return DEFAULT_DISTANCE
    else:
        return disMatrix[x, y]


h = 79
w = 79
path_x = []
path_y = []
while h > -1 and w > -1:
    current = disMatrix[h, w]
    # print(current)
    path_x.append(w)
    path_y.append(h)
    if h == 0 and w == 0:
        break

    left = get_distance(h, w - 1) if current > get_distance(h, w - 1) else DEFAULT_DISTANCE
    right = get_distance(h, w + 1) if current > get_distance(h, w + 1) else DEFAULT_DISTANCE
    top = get_distance(h - 1, w) if current > get_distance(h - 1, w) else DEFAULT_DISTANCE
    bottom = get_distance(h + 1, w) if current > get_distance(h + 1, w) else DEFAULT_DISTANCE
    # print(str(left) + " " + str(right) + " " + str(top) + " " + str(bottom))
    mins = min(left, right, top, bottom)
    if mins == left:
        w = w - 1
    elif mins == right:
        w = w + 1
    elif mins == top:
        h = h - 1
    elif mins == bottom:
        h = h + 1

# 限制坐标轴

plt.axis([-1, 81, -1, 81])
plt.pause(1)
# 使用红色-星状标记需要绘制的点
for i in range(len(path_x)):
    plot(path_x[i], path_y[i], 'r*')
    plt.pause(0.005)
# 1）控制颜色
# 颜色之间的对应关系为
# b---blue   c---cyan  g---green    k----black
# m---magenta r---red  w---white    y----yellow
# ∈
# correct 将数组中的前两个点进行连线 x0,y0 -- x1,y1   x[0, 2] == x ∈ [0, 2)
# plot(path_x[:], path_y[:])
# show()
# 打点 Dijkstra 遍历过程
for i in range(len(path_x)):
    x = len(path_x) - i
    plot(path_x[x - 2: x], path_y[x - 2: x], 'b')
    plt.pause(0.005)

plt.show()
