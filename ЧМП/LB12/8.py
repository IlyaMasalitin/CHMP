from scipy import integrate 
import math
eps = 0.001
def f1(x): 
    return math.sin(x**2-1)/2*math.sqrt(x)

def simpson(a,b,n): 
    h = (b - a) / n 
    integr = f1(a) + f1(b) 
    for i in range(1,n): 
        k = a + i*h 
        if i%2 == 0: 
            integr += 2 * f1(k) 
        else: 
            integr += 4 * f1(k) 
    integr *= h/3 
    return integr 
if abs(simpson(2.1,1.3,2*8) -simpson(2.1,1.3,8))/ 15. <= eps: 
   print("Simpsone method:",round (simpson(2.1,1.3,8), 5)) 
v,err = integrate.quad(f1,2.1,1.3)
print("Check for the simpsone method= ",round(v, 5)) 
