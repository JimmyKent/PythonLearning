from heapq import *


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

    def __ge__(self, other):  # operator >=
        return self.distance >= other.distance

    def __le__(self, other):  # operator <=
        return self.distance <= other.distance

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ", " + str(self.distance) + ")"

    def __repr__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ", " + str(self.distance) + ")"


node1 = Node(1, 1, 2)
node2 = Node(1, 1, 3)
print(node1 == node2)

nodes = []
nodes.append(node2)
nodes.append(node1)
heapify(nodes)
heappush(nodes, Node(2, 1, 10))

bottom = Node(2, 1, 3)
if bottom in nodes:
    temp = 1000
    bottom.distance = temp
    nodes.remove(bottom)
    nodes.append(bottom)
    heapify(nodes)

test = heappop(nodes)
print(test)
test2 = heappop(nodes)
print(test2)
test2 = heappop(nodes)
print(test2)
print(len(nodes))

