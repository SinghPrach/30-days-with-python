# A probability distribution in which the random variable X can take any value is continuous random variable.

from scipy.stats import norm
import numpy as np
print norm.cdf(np.array([1,-1., 0, 1, 3, 4, -2, 6]))

# To find the median of a distribution, we can use the Percent Point Function (ppf).

from scipy.stats import norm
print norm.ppf(0.5)

# To generate a sequence of random variates.

from scipy.stats import norm
print norm.rvs(size = 5)
