import numpy as np
from sympy import *
from scipy.optimize import approx_fprime

x = symbols('x')
y = symbols('y')

# first function
f = 2 * x ** 2 * y ** 3 + 1 / x + y ** 2 * x + 7
f1x = diff(f, x)
print(format(f1x))

f1y = diff(f, y)
print(format(f1y))

# second function
f = x ** 2 * y - sin(x * y) + cos(x ** 2) + 6 * y
f1x = diff(f, x)
print(format(f1x))

f1y = diff(f, y)
print(format(f1y))


# gradient of the first function
def func(t):
    return 2 * t[0] ** 2 * t[1] ** 3 + 1 / t[0] + t[1] ** 2 * t[0] + 7


eps = np.sqrt(np.finfo(float).eps)
grad = approx_fprime([1, 2], func, [eps, eps])
print(grad)
