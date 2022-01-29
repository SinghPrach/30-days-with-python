#Unconstrained minimization (method='brent')

from scipy.optimize import minimize_scalar
f = lambda x: (x - 2) * (x + 1)**2
res = minimize_scalar(f, method='brent')
print(res.x)

#Bounded minimization
from scipy.special import j1
res = minimize_scalar(j1, bounds=(4, 7), method='bounded')
res.x
