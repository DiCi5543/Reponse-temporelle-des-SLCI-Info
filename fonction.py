import math as ma
from sympy import symbols, Eq

def delta(x, A=1):
    if x == 0:
        return(A)
    else:
        return (0)

def u(x, d=100):
    if x < d and x > 0:
        return(1)
    else:
        return(0)

def imp(x, inv):
    if inv == 0:
        return(delta(x))
    else:
        return(1)

def ech(x, d, inv):
    if inv == 0:
        return(u(x, d))
    else:
        return(1/s)

def ramp(x, d, a, inv):
    if inv == 0:
        return(a*x*u(x, d))
    else:
        return(a/s**2)

def puiss(x, d, n, inv):
    if inv == 0:
        return(x**n*u(x, d))
    else:
        return((ma.factorial(n))/(s**(n+1)))

def exp(x, d, a, inv):
    if inv == 0:
        return(ma.exp((-a)*x)*u(x, d))
    else:
        return(1/(s+a))

def texp(x, d, a, inv):
    if inv == 0:
        return(x*ma.exp((-a)*x)*u(x, d))
    else:
        return(1/(s+a)**2)

def sin(x, d, w, inv):
    if inv == 0:
        return(ma.sin(w*x)*u(x, d))
    else:
        return(w/(s**2+w**2))

def cos(x, d, w, inv):
    if inv == 0:
        return(ma.cos(w*x)*u(x, d))
    else:
        return(s/(s**2+w**2))

def sinam(x, d, w, a, inv):
    if inv == 0:
        return(ma.sin(w*x)*ma.exp((-a)*x)*u(x, d))
    else:
        return(w/((s+a)**2+w**2))

def cosam(x, d, w, a, inv):
    if inv == 0:
        return(ma.cos(w*x)*ma.exp((-a)*x)*u(x, d))
    else:
        return((s+a)/((s+a)**2+w**2))