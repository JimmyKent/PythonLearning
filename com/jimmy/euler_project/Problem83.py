# 从左上角走到右下角 425185

import numpy as np
from heapq import *


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


class Node(object):
    x = 0
    y = 0
    distance = 0

    def __init__(self, x, y, distance):
        self.x = x
        self.y = y
        self.distance = distance

    def __eq__(self, other):
        return self.x * 100 + self.y == other.x * 100 + other.y

    def __lt__(self, other):  # operator <
        return self.distance < other.distance

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ", " + str(self.distance) + ")"

    def __repr__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ", " + str(self.distance) + ")"


def refresh(n):
    return min(get_distance(n.x, n.y - 1), get_distance(n.x, n.y + 1),
               get_distance(n.x - 1, n.y), get_distance(n.x + 1, n.y), DEFAULT_DISTANCE)


def get_distance(x, y):
    if (y < 0) or y >= 80 or x < 0 or x >= 80:
        return DEFAULT_DISTANCE
    else:
        return disMatrix[x, y]


# ----------------------------------


original = read_data("p81-82-83_matrix.txt", ',')

DEFAULT_DISTANCE = 100000000

disMatrix = np.full(original.shape, DEFAULT_DISTANCE, dtype=int)

# print(disMatrix)
# print(original)

# init
disMatrix[0, 0] = original[0, 0]

U = []
# XXX
for h in range(80):
    for w in range(80):
        U.append(Node(h, w, DEFAULT_DISTANCE))

U.remove(Node(0, 0, DEFAULT_DISTANCE))
U.remove(Node(0, 1, DEFAULT_DISTANCE))
U.remove(Node(1, 0, DEFAULT_DISTANCE))

U.append(Node(0, 1, original[0, 1] + original[0, 0]))
U.append(Node(1, 0, original[1, 0] + original[0, 0]))
disMatrix[0, 1] = original[0, 1] + original[0, 0]
disMatrix[1, 0] = original[1, 0] + original[0, 0]
heapify(U)

while len(U) > 0:
    node = heappop(U)
    w = node.x
    h = node.y
    disMatrix[h, w] = node.distance

    print(node)

    if (w - 1 > 0) and w - 1 < 80:
        left = Node(h, w - 1, disMatrix[h, w - 1])
        if left in U:
            temp = refresh(left)
            disMatrix[h, w - 1] = min(original[h, w - 1] + temp, disMatrix[h, w - 1])
            left.distance = disMatrix[h, w - 1]
            U.remove(left)
            heappush(U, left)
            heapify(U)

    if (w + 1 > 0) and w + 1 < 80:
        right = Node(h, w + 1, disMatrix[h, w + 1])
        if right in U:
            temp = refresh(right)
            disMatrix[h, w + 1] = min(original[h, w + 1] + temp, disMatrix[h, w + 1])
            right.distance = disMatrix[h, w + 1]
            U.remove(right)
            heappush(U, right)
            heapify(U)

    if (h - 1 > 0) and h - 1 < 80:
        top = Node(h - 1, w, disMatrix[h - 1, w])
        if top in U:
            temp = refresh(top)
            disMatrix[h - 1, w] = min(original[h - 1, w] + temp, disMatrix[h - 1, w])
            top.distance = disMatrix[h - 1, w]
            U.remove(top)
            heappush(U, top)
            heapify(U)

    if (h + 1 > 0) and h + 1 < 80:
        bottom = Node(h + 1, w, disMatrix[h + 1, w])
        if bottom in U:
            temp = refresh(bottom)
            disMatrix[h + 1, w] = min(original[h + 1, w] + temp, disMatrix[h + 1, w])
            bottom.distance = disMatrix[h + 1, w]
            U.remove(bottom)
            heappush(U, bottom)
            heapify(U)

print(disMatrix[79, 79])
