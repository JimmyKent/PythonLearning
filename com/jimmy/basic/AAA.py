# 数组
# 矩阵
# 元组
# 字典
# 多维数组

# matrix
import numpy as np

disMatrix = np.full([8, 9], 100, dtype=int)

print(disMatrix)
print(disMatrix.shape[1])
h = len(disMatrix)
w = len(disMatrix[0])

print(h)
print(str(w) + "  ")


