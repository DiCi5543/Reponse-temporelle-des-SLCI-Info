import math as ma
import matplotlib.pyplot as plt
from sympy import symbols, Eq
#import fonction as f
import numpy as np


s = symbols("s")

#------------------------------------------------------

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


#---------------------------------------------------------

N = []
D = [1,0,4,0,3]
E = []
roots = np.roots(D)
#entrée : fct de transfert connue/fct temporelle excitatrice connue
#stocker numérateur / dénominateur dans deux listes

#demande à l'opérateur d'entrer les coeff un nulmérateur puis dénominateur
     #np.roots(r1,r2,r3) pour déterminer racines de D


def x_dans_L(x,L):

    """
    X dans L : vérifie si l'élément x est dans la liste L

    Arguments :

        x (int,float,str) : x est l'élément à trouver
        L (list) : liste

    Résultat :

        True si x est dans L
        False sinon
    """

    for e in L:
        if e == x:
            return(True)
    return(False)


def racines_conjuguees():

    """
    racines_conjuguées : trouve les racines complexes  du polynôme de D qui peuvent être assemblées

    Arguments :

        racines (list) : liste des racines du polynôme

    Résultat :

        conj (list) : liste contenant les doublets des indices des racines complexes conjuguées
    """
    conj = []
    Im = []
    for e in roots:
        Im.append(np.imag(e))

    for i in range(len(Im)):
        for k in range(len(Im)):
            if Im[i] == (-1)*(Im[k]):
                if x_dans_L([k,i],conj) == False:
                    conj.append([i,k])

    return(conj)

def polyracine(index, roots):
    """
    polyracine : renvoie les coefficients du polynôme (X-root[index])

    Argument :

        index (int) : indice de la racine choisi
        roots (list) : liste des racines

    Résultat :

        (list) : des coefficients du polynôme
    """
    return([1,(-1)*(roots[index])])

def produit_conjuguees(listeconjugues,roots):
    """
    produit_conjuguees : la liste des produits de 2 racine racines complexes conjuguees

    Arguments :

        listeconjugues (list) : liste des indices correspondant à des complexes conjugués
        roots (list) : liste des racines du polynôme

    Résultat :

        (list) : renvoie la liste des coefficients des polynômes obtenus par le produits de 2 complexes conjugués
    """
    prod_racines_conjuguees = []
    for e in listeconjugues:
        prod_racines_conjuguees.append([np.polymul(polyracine(e[0],roots),polyracine(e[1],roots))])
    return(prod_racines_conjuguees)

#print(np.roots(D))
#print(racines_conjuguees())
print(produit_conjuguees(racines_conjuguees(),roots)[0][0])
print(produit_conjuguees(racines_conjuguees(),roots)[1])


#si racine réelle --> (X - r)
#pour chaque racine réelle on a un Ak associé au numérateur à identifier

#si racine imaginaire, on multiplie (X - r)(X - r/) --> X²+bX+c
#pour chaque racine complexe conjuguées, on a Bk*s + Ck comme numératueur à identifier

#liste de coeff : coeff de N associés au coeff de : (somme(Ak/X-r) + somme(Bk*X+Ck/X²+bX+c))*(produit(X-r)*produit(X²+bX+c))
# on a liste de coeff associées aux puissances


def S(t):
    return(exp(t,20,-1,0))

def g(t):
    return(exp(t,20,-1,0)*cosam(t,20,2,2,0))

X = [i/100 for i in range(0,1000)]
Y = [S(x) for x in X]
Z = [g(x) for x in X]

plt.figure()

plt.subplot(211)
plt.plot(X,Y)
plt.grid()

plt.subplot(212)
plt.plot(X,Z)
plt.grid()

plt.suptitle("Fonction")
plt.show()


