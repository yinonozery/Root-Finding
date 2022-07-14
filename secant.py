# Yinon Ozery
# Secant Method

import math
import matplotlib.pyplot as plt
import numpy as np

def secantMethod(f,a,b,err,M):
    for n in range(1, M+1):
        c = a - f(a)*(b - a) / (f(b) - f(a)) # Intersection with x axis
        if ((n > 1) and (math.fabs(c-d) < err)): # |x(n+1)-x(n)| < max error
            print('Max No. of iterations:', M)
            print('Actual No. of iterations:', n - 1)
            return c
        d = c
        f_c = f(c)
        if f_c == 0: #root found
            print('Found exact root, x(%d):' %n)
            print(c)
            return c
        else:
            a = b
            b = c
        print('x(%d):' %n, c,'\t', 'f(x%d):' %n, f(c))
        
    print('Appropriate root (%d):' %n)
    print(c)
    return c

#Function
func = input("Enter a polynomial function: ")
p = lambda x: eval(func)

print("Enter two initials values of x0 and x1, they should be close to the desired root.")
x0 = float(input("x0: "))
x1 = float(input("x1:"))

m = int(input("Enter the number of max iterations: "))

xmark = secantMethod(p,x0,x1,1.0e-16,m)

#Graph
x = np.linspace(0, 10, 50, endpoint = True)
y = eval(func)

plt.title('Approximate root with Secant Method')
plt.plot(x, y, '-g')
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')
x0 = [xmark]
y0 = [p(xmark)]
plt.plot(x0,y0,'o')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()
