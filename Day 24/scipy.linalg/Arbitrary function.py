from scipy import special, linalg
import numpy as np

rng = np.random.default_rng()
A = rng.random((3, 3))
B = linalg.funm(A, lambda x: special.jv(0, x))

print('A = ', A)
print('B = ', B)
print('linalg.eigvals(A) = ', linalg.eigvals(A))
print('special.jv(0, linalg.eigvals(A))  = ', special.jv(0, linalg.eigvals(A)))
print('linalg.eigvals(B) = ', linalg.eigvals(B))
