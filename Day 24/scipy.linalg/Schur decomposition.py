# Schur decomposition
from scipy import linalg
import numpy as np

A = np.mat('[1 3 2; 1 4 5; 2 3 6]')
T, Z = linalg.schur(A)
T1, Z1 = linalg.schur(A, 'complex')
T2, Z2 = linalg.rsf2csf(T, Z)

print('T = ', T)
print('T2 = ', T2)
print('abs(T1 - T2) = ', abs(T1 - T2))  # different
print('abs(Z1 - Z2)  = ', abs(Z1 - Z2) )  # different
print('abs(A - Z*T*Z.H) = ', abs(A - Z*T*Z.H))  # Same
print('abs(A - Z1*T1*Z1.H) = ', abs(A - Z1*T1*Z1.H))  # Same
print('abs(A - Z2*T2*Z2.H) = ', abs(A - Z2*T2*Z2.H))  # Same
