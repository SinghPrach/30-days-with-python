# Example 1

import numpy as np
from scipy.linalg import eig, eigh
from scipy.sparse.linalg import eigs, eigsh
np.set_printoptions(suppress=True)
rng = np.random.default_rng()

X = rng.random((100, 100)) - 0.5
X = np.dot(X, X.T)  # create a symmetric matrix
