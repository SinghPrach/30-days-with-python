import numpy as np
from scipy import linalg

A = np.array([[1, 3, 5], [2, 5, 1], [2, 3, 8]])
Inv_A = linalg.inv(A)  # Built-in function for finding inverse
print('Inverse of matrix A is = ', Inv_A)
A_obtained = A.dot(linalg.inv(A))  # to double check
print('Value of A is = ', A_obtained)
      
