import numpy as np
import math
a = np.matrix('2 3 4; 1 0 6; 7 8 9')
a_det = np.linalg.det(a) 
print(format(a_det, '.9g'))
