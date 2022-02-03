# Singular value decomposition
import numpy as np
from scipy import linalg

A = np.array([[1, 2, 3], [4, 5, 6]])
print('A = ', A)

M, N = A.shape
U, s, Vh = linalg.svd(A)
Sig = linalg.diagsvd(s, M, N)
U, Vh = U, Vh
print('U = ', U)

print('Sig = ', Sig)

print('Vh = ', Vh)

print('U.dot(Sig.dot(Vh)) = ', U.dot(Sig.dot(Vh)))  # check computation
