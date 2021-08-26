# Aproximación Polinomio de Taylor alrededor de x0
# f(x) en forma simbólica con sympy
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

# INGRESO --------------------
x = sym.Symbol('x')
fx = sym.exp(x)*sym.cos(x) + 1

x0 = 0
n  = 3 # grado de polinomio

# Intervalo para Gráfica
a = 0
b = np.pi
muestras = 21

# PROCEDIMIENTO  -------------
# construye polinomio Taylor
k = 0 # contador de términos
polinomio = 0
while (k <= n):
    derivada   = fx.diff(x,k)
    derivadax0 = derivada.subs(x,x0)
    divisor   = np.math.factorial(k)
    terminok  = (derivadax0/divisor)*(x-x0)**k
    polinomio = polinomio + terminok
    k = k + 1

# forma lambda para evaluación numérica
fxn = sym.lambdify(x,fx,'numpy')
pxn = sym.lambdify(x,polinomio,'numpy')

# evaluar en intervalo para gráfica
xi = np.linspace(a,b,muestras)
fxi = fxn(xi)
pxi = pxn(xi)

# SALIDA  --------------------
print('polinomio p(x)=')
print(polinomio)
print()
sym.pprint(polinomio)

# Gráfica
plt.plot(xi,fxi,label='f(x)')
plt.plot(xi,pxi,label='p(x)')
# franja de error
plt.fill_between(xi,pxi,fxi,color='yellow')
plt.xlabel('xi')
plt.axvline(x0,color='green', label='x0')
plt.axhline(0,color='grey')
plt.title('Polinomio Taylor: f(x) vs p(x)')
plt.legend()
plt.show()