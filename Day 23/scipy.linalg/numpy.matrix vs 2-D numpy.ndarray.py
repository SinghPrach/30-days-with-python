#Example 1
import numpy as np

A = np.mat('[1 2;3 4]')
print('A = ', A)

print('A X I = ', A.I)  # A.I = matrix A inverse

b = np.mat('[5 6]')

print('b =', b)

print('bT = ', b.T)    #B.T = matrix B transpose

print('A*b.T = ', A*b.T)

# Example 2
import numpy as np
from scipy import linalg

A = np.array([[1, 2], [3, 4]])
print('A = ', A)
linalg.inv(A)
print('linalg.inv(A) = ', linalg.inv(A))
b = np.array([[5, 6]])  # 2D array
print('b = ', b)  # array([[5, 6]])
print('b.T = ', b.T)  # array([[5],[6]])
print('A*b = ', A * b)  # A * b  # not matrix multiplication!
# array([[5, 12],      [15, 24]])
print('A.dot(b.T) = ', A.dot(b.T))  # matrix multiplication
# array([[17],[39]])

b = np.array([5, 6])  # 1D array
print('b.T = ', b.T)  # not matrix transpose!
print('A.dot(b) = ', A.dot(b))  # does not matter for multiplication
