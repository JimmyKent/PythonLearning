# 最小堆测试
# http://fornote.blogspot.hk/2009/04/python.html
from heapq import *
import heapq

# heap = [2, 1, -1, 9, 8]
# heapify(heap)
# print(heap)
#
# heappush(heap, 3)
# print(heap)
# heappush(heap, 10)
# print(heap)
#
# heapify(heap)
# print(heap)
#
# heappop(heap)
# print(heap)
# heappop(heap)
# print(heap)
# heappop(heap)
# print(heap)
# heappop(heap)
# print(heap)

'''
[-1, 1, 2, 9, 8]
[-1, 1, 2, 9, 8, 3]
[-1, 1, 2, 9, 8, 3, 10]
[-1, 1, 2, 9, 8, 3, 10]
[1, 8, 2, 9, 10, 3]
[2, 8, 3, 9, 10]
[3, 8, 10, 9]
[8, 9, 10]
'''


class Node:
    x = 0
    y = 0
    distance = 0

    def __eq__(self, other):
        return self.x * 100 + self.y == other.x * 100 + other.y

    def __lt__(self, other):  # operator <
        return self.x * 100 + self.y < other.x * 100 + other.y

    def __ge__(self, other):  # oprator >=
        return self.x * 100 + self.y >= other.x * 100 + other.y

    def __le__(self, other):  # oprator <=
        return self.x * 100 + self.y <= other.x * 100 + other.y

    # def __cmp__(self, other):
    #     # call global(builtin) function cmp for int
    #     return cmp(self.x * 100 + self.y, other.x * 100 + other.y)

    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + "," + str(self.distance)


node1 = Node()
node1.x = 2
node2 = Node()
node2.x = 3
print(node1 == node2)




nodes = []
nodes.append(node1)
nodes.append(node2)

if node1 in nodes:
    nodes.remove(node1)
    heappush(nodes, node1)

heapify(nodes)
test = heappop(nodes)
print(test.x)
test2 = heappop(nodes)
print(test2.x)

