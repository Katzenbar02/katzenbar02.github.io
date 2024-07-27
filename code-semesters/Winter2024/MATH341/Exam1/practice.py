import numpy as np
from sympy import Matrix
A = np.array([
    [0, 1, 3, 0, -4, 1, 0],
    [1, 1, 1, 0, -1, 0, 0],
    [1, 0, -2, 1, 8, -1, -1],
    [1, -1, -5, 1, 12, 1, -1],
    [1, 1, 1, 1, 4, 0, -1],
    [-1, 1, 5, 1, -2, 0, 0]
])

B = Matrix(A).rref()[0].tolist()

print(B)
