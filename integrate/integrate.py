from sympy import *
 
x = symbols('x')
n = symbols('n')
a = symbols('a')
 
def Deinteg(Func):
    print('The integration of ',Func,' is: \n')
    print(integrate(Func,x),'\n')
 
f = x**2*sin(n*pi*x/a)
 
Deinteg(f)