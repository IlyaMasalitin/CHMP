import numpy as np
from scipy import integrate as intgr
import matplotlib.pyplot as plt   
from scipy import integrate,interpolate as intrpl
s=[25, 35, 45, 30, 60, 120, 100, 100, 70, 75, 80, 65]
t=(np.linspace(0,11,12))
print(t)
plt.plot(t,s,'d', t, s, 'teal')
plt.xticks(np.arange(0, 12, step=1))
plt.yticks(np.arange(0, 140, step=10))
f = intrpl.interp1d(t, s,kind='cubic')
g = intrpl.interp1d(t, s,kind='quadratic')
xn = np.linspace(0, 11,10000)
v,e = intgr.quad(f,11,0) 
print("Integral (kind='cubic)'= ",round(v, 5)) 
v,e = intgr.quad(g,11,0) 
print("Integral (kind='quadratic')'= ",round(v, 5)) 
y1n = f(xn)
y2n = g(xn)
plt.xlabel('time')
plt.ylabel('speed')
plt.legend(['точки','графік'])
plt.grid()
plt.show()