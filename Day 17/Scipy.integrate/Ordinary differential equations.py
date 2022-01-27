from scipy.integrate import solve_ivp
from scipy.special import gamma, airy
y1_0 = +1 / 3**(2/3) / gamma(2/3)
y0_0 = -1 / 3**(1/3) / gamma(1/3)
y0 = [y0_0, y1_0]
def func(t, y):
    return [t*y[1],y[0]]

t_span = [0, 4]
sol1 = solve_ivp(func, t_span, y0)
print("sol1.t: {}".format(sol1.t))
