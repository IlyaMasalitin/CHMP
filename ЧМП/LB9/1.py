from scipy.interpolate import CubicSpline
import numpy as np
import matplotlib.pyplot as plt
x = [0,  0.2,  0.4  ,0.6,  0.8  ,1  ,1.2,  1.4  ,1.6,  1.8,  2,  2.3,  2.4,  2.6,  2.8,  3  ,3.3,  3.4  ,3.6  ,3.8,  4,  4.2,  4.4,  4.5]
y = [-0.40456229,   -0.005870931,   0.961520763,    2.118479237,    3.085870931,    3.48456229, 2.935419754,    1.059309767,    0.540835223,    -1.678790308,   -4.433433895,   -9.46003428,    2.070386433,    2.755465244,    3.834294402,    5.356484808,    5.645238566,    6.023762423,    6.632547925,    6.967618577,    6.937736093,    6.451662191,    5.418158587,    4.667608683]

#ascending order
if np.any(np.diff(x) < 0):
    indexes = np.argsort(x).astype(int)
    x = np.array(x)[indexes]
    y = np.array(y)[indexes]

f = CubicSpline(x, y, bc_type='natural')
x_new = np.linspace(min(x), max(x), 100)
y_new = f(x_new)

plt.plot(x_new, y_new)
plt.scatter(x, y)
plt.title('Cubic Spline Interpolation')
plt.show()
