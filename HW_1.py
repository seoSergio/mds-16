import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 1])
y = np.array([2, 0])
z = np.array([0, 2])
print('X:')
print(x)
print('Y:')
print(y)
print('Z:')
print(z)

k = x + y + z
print('')
print('K:')
print(k)

plt.figure()
plt.title('Vectors visualization as dots.')
plt.plot(x[0], x[1], 'o', label='x')
plt.plot(y[0], y[1], 'o', label='y')
plt.plot(z[0], z[1], 'o', label='z')
plt.plot(k[0], k[1], 'o', label='k')
plt.grid()
plt.legend()
plt.show()

cos_xy = np.dot(x, y) / (np.linalg.norm(x) * np.linalg.norm(y))
angle_xy_rad = np.arccos(cos_xy)
angle_xy_deg = np.degrees(angle_xy_rad)

print("Angle between vectors X and Y is {0} degrees.".format(round(angle_xy_deg, 2)))
