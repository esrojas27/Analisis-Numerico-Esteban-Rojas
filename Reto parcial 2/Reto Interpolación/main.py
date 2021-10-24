import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np
import math
from Bezier import Bezier
from numpy import array as a
import mpl_toolkits.mplot3d.art3d as art3d


def areaParaboloide():
    r = 2.1
    h = 1
    return 0.5236 * (r / h ** 2) * (((r ** 2 + 4 * h ** 2) ** (3 / 2)) - r ** 3)


def areaCilindro():
    r = 0.76
    h = 0.4
    return math.pi * r ** 2 * h


def areaEsfera():
    r = math.sqrt(2)
    return 4 * r ** 2 * math.pi


def areaPico(l=1):
    area = (l * l / 2) * 3
    return area


def volumenEsfera():
    r = math.sqrt(2)
    return 4 / 3 * r ** 3 * math.pi


def volumenParaboloide():
    r = 2.1
    h = 1
    return (math.pi * r ** 2 * h) / 2


def volumenCilindro():
    h = 0.4
    return areaCilindro() * h


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')#proyección en 3d

h = -2  # Altura (z)
b = 0.76  # Radio 1

# base
def cilindro(curvaNivel=False):
    h = 0
    b = 0.76  # Radio 1
    for i in range(0, 4):
        p = Circle((0, 0), b, color="green", fill=curvaNivel)#proyección del circulo
        ax.add_patch(p)
        art3d.pathpatch_2d_to_3d(p, z=h)
        h = h + 0.1


def esfera(curvaNivel=False):
    b = 0.0  # Radio 2
    # esfera
    for i in np.arange(-1, 1.4, 0.1):
        p = Circle((0, 0), b, color="black", fill=curvaNivel)
        ax.add_patch(p)
        art3d.pathpatch_2d_to_3d(p, z=i + 1.1)
        b = 2 - (i * i)
        print(b)


def paraboloide(curvaNivel=False):
    # paraboloide
    radio = 0.79
    for i in np.arange(1, 1.7, 0.1):
        p = Circle((0, 0), radio, color="blue", fill=curvaNivel)
        ax.add_patch(p)
        if i < 0.5:
            radio -= 0.1
        else:
            radio += 0.1
        art3d.pathpatch_2d_to_3d(p, z=i + 1.5)


# pico
def pico(curvaNivel=False):
    aumento = 0.1
    rango = 6
    aumentoX = 0.4
    h = 2.6
    p = 1
    if curvaNivel:
        aumento = 0.025
        rango = 18
        aumentoX = 0.1

    b = 0.6
    x = 0
    for i in range(0, rango):
        points_set_1 = a([[-b, -1, h], [-1, -p - x, h], [1, -p - x, h], [b, -1, h]])
        t_points = np.arange(0, 1, 0.01)
        curve_set_1 = Bezier.Curve(t_points, points_set_1)
        ax.plot(curve_set_1[:, 0], curve_set_1[:, 1], curve_set_1[:, 2], color="purple")
        h = h + aumento
        x = x + aumentoX


cilindro()
esfera()
paraboloide()
pico()

area = areaPico() + areaCilindro() + areaEsfera() + areaParaboloide() - (abs(areaCilindro() - areaEsfera())) - (
    abs(areaParaboloide() - areaEsfera()))
volumen = volumenCilindro() + volumenEsfera() + volumenParaboloide() - (abs(volumenCilindro() - volumenEsfera())) - (
    abs(volumenParaboloide() - volumenEsfera()))
print("el área de la jarra es: ", area)
print("el volumen de la jarra es: ", volumen)

#setear las aristas
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_zlim(-1, 5)
ax.set_xlabel('eje x')
ax.set_ylabel('eje y')
ax.set_zlabel('eje z')
plt.show()