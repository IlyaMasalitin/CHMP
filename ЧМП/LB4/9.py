
import numpy as np
import math
A = np.matrix('-2   1   4; 1 4 -1; 2 3 1')
print('A=',A)
B = np.matrix('-2; -1; 0')
print('A=', A)
print('B=',B)
a_inv = np.linalg.inv(A)
print(a_inv)
x = a_inv.dot(A)
print('X=',x)
