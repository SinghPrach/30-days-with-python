# A uniform distribution can be generated using the uniform function.

from scipy.stats import uniform
print uniform.cdf([0, 1, 2, 3, 4, 5], loc = 1, scale = 4)

