import numpy as np
from pylab import *
from matplotlib import pyplot as plt
from matplotlib import animation
plt.rcParams['animation.ffmpeg_path'] = '/usr/local/Cellar/ffmpeg/3.4.1/bin/ffmpeg'

disMatrix = np.loadtxt("/Users/jinguochong/PycharmProjects/PythonLearning/com/jimmy/euler_project/Problem83_distance_matrix.txt", delimiter=' ')

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

# 使用红色-星状标记需要绘制的点
plot(path_x, path_y, 'r*')
# 1）控制颜色
# 颜色之间的对应关系为
# b---blue   c---cyan  g---green    k----black
# m---magenta r---red  w---white    y----yellow
# ∈
# correct 将数组中的前两个点进行连线 x0,y0 -- x1,y1   x[0, 2] == x ∈ [0, 2)
# plot(path_x[:], path_y[:])
# 打点 Dijkstra 遍历过程
for i in range(len(path_x)):
    x = len(path_x) - i
    plot(path_x[x - 2: x], path_y[x - 2: x], 'b')
    plt.pause(0.005)


fig = plt.figure()
ax = plt.axes(xlim=(0, 2), ylim=(-2, 2))
line = ax.plot([], [], lw=2)


# initialization function: plot the background of each frame
def init():
    line.set_data([], [])
    return line,


# animation function.  This is called sequentially
def animate(i):
    x = np.linspace(0, 2, 1000)
    y = np.sin(2 * np.pi * (x - 0.01 * i))
    line.set_data(x, y)
    return line,


# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=200, interval=20, blit=True)

# save the animation as an mp4.  This requires ffmpeg or mencoder to be
# installed.  The extra_args ensure that the x264 codec is used, so that
# the video can be embedded in html5.  You may need to adjust this for
# your system: for more information, see
# http://matplotlib.sourceforge.net/api/animation_api.html

anim.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])

plt.show()
