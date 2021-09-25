import numpy as np


lst1 = [[0, 1, 2], [3, 4, 5]]
lst2 = [[0, 2, 4], [6, 8, 10]]

mat1 = np.matrix(lst1)
mat2 = np.matrix(lst2)
print(mat1)

# 転地
print(mat1.T)


print(mat1 + mat2)
# [[0  3  6]
#  [9 12 15]]

print(mat1 - mat2)
# [[0 -1 -2]
#  [-3 -4 -5]]

# 要素ごとの積
print(np.multiply(mat1, mat2))
# [[0  2  8]
#  [18 32 50]]

# これはエラーになります. なぜなら， matrix 型なので（行列積なので）
print(mat1 * mat2)
