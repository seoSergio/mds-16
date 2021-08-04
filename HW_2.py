# Level 0
import numpy as np

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
A1 = A + np.eye(3)
print('A1:')
print(A1)

v = np.array([[1], [2], [3]])
A1v = A1 @ v
print('A1v:')
print(A1v)

A1i = np.linalg.inv(A1)
print('A1i:')
print(A1i)
print('Double check if the inverse matrix is correctly calculated. A1 @ A1i:')
print(A1 @ A1i)

# Level 1
import numpy as np
import matplotlib.pyplot as plt

A = [
    [-100, -100, 1],
    [-100, 100, 1],
    [100, 100, 1],
    [0, 0, 1],
    [100, -100, 1],
    [-100, -100, 1]
]


def plot_object(arr: np.array, x_lim = [-200, 200], y_lim = [-200, 200]):
    x = arr[:, 0]
    y = arr[:, 1]
    plt.plot(x, y)
    plt.xlim(x_lim)
    plt.ylim(y_lim)
    plt.show()


A = np.array(A)
plot_object(A)

T_half_size = np.array([
    [0.5, 0, 0],
    [0, 0.5, 0],
    [0, 0, 1]])
A_half_size = A @ T_half_size
print('A_half_size:')
print(A_half_size)
plot_object(A_half_size)

angle_rad = np.deg2rad(130)
T_rotation = np.array([
    [np.cos(angle_rad), -np.sin(angle_rad), 0],
    [np.sin(angle_rad), np.cos(angle_rad), 0],
    [0, 0, 1]
])
A_rotated = A @ T_rotation
print('A_rotated:')
print(A_rotated)
plot_object(A_rotated)

T_Householder = np.array([
    [0, 1, 0],
    [1, 0, 0],
    [0, 0, 1]
])
A_reflected = A @ T_Householder
print('A_reflected:')
print(A_reflected)
plot_object(A_reflected)

x_shift = 200
y_shift = 300
T_shift = np.array([
    [x_shift, y_shift, 0],
    [x_shift, y_shift, 0],
    [x_shift, y_shift, 0],
    [x_shift, y_shift, 0],
    [x_shift, y_shift, 0],
    [x_shift, y_shift, 0]
])
T_scale = np.array([
    [0.5, 0, 0],
    [0, 1.2, 0],
    [0, 0, 1]
])
A_transformed = A @ T_scale + T_shift
print('A_transformed:')
print(A_transformed)
plot_object(A_transformed, [-200 + x_shift, 200 + x_shift], [-200 + y_shift, 200 + y_shift])
