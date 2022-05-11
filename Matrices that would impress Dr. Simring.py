# matrix = [
#      [1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9],

#  ]
# matrix [0][1] = 20
# print(matrix[0][1])

# matrix = [
#      [1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9],

# ]
# for row in matrix:
#      for item in row:
#          print(item)


# matrix1 = ([0, 1, 0],
#         [0, 0, -1],
#         [1, -1, -2])
# matrix2 = ([3, 0, 1],
#         [1, 0, 0],
#         [0, -2, 0])

# res = [[0 for x in range(3)] for y in range(3)]

# for i in range(len(matrix1)):
#     for j in range(len(matrix2[0])):
#         for k in range(len(matrix2)):

#             res[i][j] += matrix1[i][k] * matrix2[k][j]

# print (res)

from numpy.linalg import matrix_power 
import numpy as np
# matrix1 = np.array([0.6, 0.3],[0.4, 0.7])
# matrix2 = np.array([0.6, 0.3],[0.4, 0.7])

matrix3 = np.array([[0.5, 0.7], [0.5, 0.3]])

# res = [[0 for x in range(2)] for y in range(2)]

# for i in range(len(matrix1)):
#     for j in range(len(matrix2[0])):
#         for k in range(len(matrix2)):

#             res[i][j] += matrix1[i][k] * matrix2[k][j]

number3 = matrix_power(matrix3, 100)

print (number3)

input()