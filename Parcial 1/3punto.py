import math
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x-np.cos(x)


# Se reescribe f(x)=0 a x = g(x)
def g(x):
    return 1 / math.sqrt(1 + x)


# Implementando Punto fijo
def fixedPointIteration(x0, e, N):
    print('\n\n*** PUNTO FIJO ITERATION ***')
    step = 1
    flag = 1
    condition = True
    while condition:
        x1 = g(x0)
        print('Iteration-%d, x1 = %0.6f and f(x1) = %0.6f' % (step, x1, f(x1)))
        x0 = x1

        step = step + 1

        if step > N:
            flag = 0
            break

        condition = abs(f(x1)) > e

    if flag == 1:
        print('\nRequired root is: %0.8f' % x1)
    else:
        print('\nNo Convergente.')


# Input Section
x0 = input('Ingresar Guess: ')
e = input('Error: ')
N = input('Paso Maximo: ')

# Convertiendo x0 y e to float
x0 = float(x0)
e = float(e)

# Convertiendo N a integer
N = int(N)

fixedPointIteration(x0, e, N)

x = np.linspace(0, 1.5, 100)
plt.plot(x, f(x))
plt.plot(x,f(x),label='f(x)')
plt.grid()
plt.show()