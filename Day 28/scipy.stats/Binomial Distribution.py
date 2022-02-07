# The binom object inherits from it a collection of generic methods and completes them with details specific for this particular distribution.

from scipy.stats import uniform
print uniform.cdf([0, 1, 2, 3, 4, 5], loc = 1, scale = 4)

----------------------------------------------------------------

from scipy import stats
import numpy as np
x = np.array([1,2,3,4,5,6,7,8,9])
print x.max(),x.min(),x.mean(),x.var()

''' Output: (9, 1, 5.0, 6.666666666666667) '''
