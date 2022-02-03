# Eigenvalues and eigenvectors
import numpy as np
from scipy import linalg
A = np.array([[1, 2], [3, 4]])
la, v = linalg.eig(A)
l1, l2 = la
print('Eigen Values are: ', l1, l2)   # eigenvalues
# (-0.3722813232690143+0j) (5.372281323269014+0j)
print('First eigenvector: ',v[:, 0])   # first eigenvector
# [-0.82456484  0.56576746]
print('Second eigenvector: ', v[:, 1])   # second eigenvector
# [-0.41597356 -0.90937671]
print(np.sum(abs(v**2), axis=0))  # eigenvectors are unitary
# [1. 1.]
v1 = np.array(v[:, 0]).T
print(linalg.norm(A.dot(v1) - l1*v1))  # check the computation
# 3.23682852457e-16
