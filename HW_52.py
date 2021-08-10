import numpy as np
from scipy.optimize import approx_fprime


def f(t):
    return (t[0] ** 2) + (t[1] ** 2)


x0 = np.array([100, 200])
learning_rate = 0.1

eps = np.sqrt(np.finfo(float).eps)
x = x0
for i in range(100):
    # Calculate gradient
    grad = approx_fprime(x, f, [eps, eps])

    # Update x with gradient
    x = np.array([
        x[0] - learning_rate * grad[0],
        x[1] - learning_rate * grad[1]
    ])

print("Minimum is in: ", x)
print("Minimum value is: ", f(x))


from scipy.optimize import minimize

res = minimize(f, x0, method='nelder-mead', options={'xtol': 1e-8, 'disp': True})
print(res)
