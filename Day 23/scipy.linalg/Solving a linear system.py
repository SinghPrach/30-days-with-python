# For solving a system of equations of the form AX = B

import numpy as np
from scipy import linalg

A = np.array([[1, 2], [3, 4]]) 
# A = array([[1, 2],[3, 4]])
b = np.array([[5], [6]])
# b = array([[5],[6]])
linalg.inv(A).dot(b)  # slow
# array([[-4. ], [ 4.5]])
A.dot(linalg.inv(A).dot(b)) - b  # check
# array([[  8.88178420e-16],      [  2.66453526e-15]])
np.linalg.solve(A, b)  # fast
# array([[-4. ],      [ 4.5]])
A.dot(np.linalg.solve(A, b)) - b  # check
# array([[ 0.],      [ 0.]])
