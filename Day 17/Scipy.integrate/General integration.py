# Integrate a bessel function jv(2.5, x) along the interval [0,4.5]
#Program 1
import scipy.integrate as integrate
import scipy.special as special

result = integrate.quad(lambda x: special.jv(2.5, x), 0, 4.5)
print(result)


#Program 2
from numpy import sqrt, sin, cos, pi
from scipy import special

I = sqrt(2/pi)*(18.0/27*sqrt(2)*cos(4.5) - 4.0/27*sqrt(2)*sin(4.5) +
                sqrt(2*pi) * special.fresnel(3/sqrt(pi))[0])

#Program 3
from scipy.integrate import quad


def integrand(x, a, b):
    return a * x ** 2 + b


a = int(input('Enter the value of a: '))
b = int(input('Enter the value of b: '))
I = quad(integrand, 0, 1, args=(a, b))
print(I)

#Program 4
from scipy.integrate import quad


def integrand(t, n, x):
    return np.exp(-x*t) / t**n
