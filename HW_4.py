import math
from scipy.misc import derivative


def f(x):
    y = x ** 5 + 4 * math.sin(2 * x) + math.cos(3 * x + 3)
    return y


def f1(x):
    y = 5 * x ** 4 + 8 * math.cos(2 * x) - 3 * math.sin(3 * x + 3)
    return y


def f2(x):
    y = 20 * x ** 3 - 16 * math.sin(2 * x) - 9 * math.cos(3 * x + 3)
    return y


dx1 = derivative(f, 1.0, dx=1e-6)
print("dx1: {}; f1(1):{}".format(dx1, f1(1.0)))
dx2 = derivative(f, 1.0, dx=1e-6, n=2)
print("dx2: {}; f2(1):{}".format(dx2, f2(1.0)))


from sympy import *
from numpy import linspace
import matplotlib.pyplot as pl

x = symbols('x')
y = sin(2 * x + 1) ** 5


y1 = diff(y, x)
print(format(y1))

lam_y1 = lambdify(x, y1, modules=['numpy'])

x_vals = linspace(-5, 5, 1000)
y_vals = lam_y1(x_vals)

pl.plot(x_vals, y_vals)
pl.show()


y2 = diff(y1, x)
print(format(y2))

lam_y2 = lambdify(x, y2, modules=['numpy'])

x_vals = linspace(-5, 5, 1000)
y_vals = lam_y2(x_vals)

pl.plot(x_vals, y_vals)
pl.show()
