from scipy import integrate 
import math
eps = 0.001
def f1(x): 
    return 1/math.sqrt(1+2*x**2)

def trap(f1,a,b,n): 
    h=(b-a)/n 
    sum=0.5*(f1(a)+f1(b)) 
    for i in range(1,n): 
        sum+=f1(a+i*h)
    return sum*h

v,err = integrate.quad(f1,1.5,0.6)
if abs (trap(f1, 1.5,0.6, 2*10) -trap(f1, 1.5,0.6, 10))/3. <= eps: 
    print("Trapetzia method:",round (trap(f1,1.5,0.6,10), 5)) 
print("Check for the trapetzia method= ",round(v, 5)) 
