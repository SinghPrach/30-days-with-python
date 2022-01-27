# Integrate a bessel function jv(2.5, x) along the interval [0,4.5]

import scipy.integrate as integrate
import scipy.special as special

result = integrate.quad(lambda x: special.jv(2.5, x), 0, 4.5)
print(result)

from numpy import sqrt, sin, cos, pi
from scipy import special

I = sqrt(2/pi)*(18.0/27*sqrt(2)*cos(4.5) - 4.0/27*sqrt(2)*sin(4.5) +
                sqrt(2*pi) * special.fresnel(3/sqrt(pi))[0])
