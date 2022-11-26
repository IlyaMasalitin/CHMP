import numpy as np
import math
a = np.matrix('1 2 3 4; -2 1 -4 3; 3 -4 -1 2;4 3 -2 -1')
a_det = np.linalg.det(a) 
print(format(a_det, '.9g'))
