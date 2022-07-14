# Yinon Ozery
# Newton-Rapson Method

import math
import matplotlib.pyplot as plt
import numpy as np

def newtonRaphsonMethod(f,d,x,err,M):
    print('x(1):', x,'\t', 'f(x1):', f(x))
    for n in range(2, M + 1):
        x_new = x - (f(x) / d(x)) # Intersection with x axis
        if (n > 1) and math.fabs(x-x_new) < err: # |x(n+1)-x(n)| < max error
            return x
        elif(f(x_new) == 0): #root found
            print('Found exact root, x(%d):' %n)
            print(x_new)
            return x_new
        x = x_new
        print('x(%d):' %n, x,'\t', 'f(x%d):' %n, f(x))
    return x

#Function
func = input("Enter a polynomial function: ")
p = lambda x: eval(func)

deriv = input("Enter the derivative of this function: ")
d = lambda x: eval(deriv)

m = int(input("Enter the number of max iterations: "))
v = float(input("Enter initial value of x, it should be close to the desired root: "))

xmark = newtonRaphsonMethod(p,d,v,1.0e-16,m)

#Graph
x = np.linspace(0, 10, 50, endpoint = True)
y = eval(func)

plt.title('Approximate root with Newton-Raphson Method')
plt.plot(x, y, '-g')
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')
x0 = [xmark]
y0 = [p(xmark)]
plt.plot(x0, y0, 'o')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()
