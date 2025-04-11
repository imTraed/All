import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, integrate

# Definir variables
x, y = symbols('x y')

# Definir la función
f = x

# Calcular la integral doble
integral_result = integrate(integrate(f, (y, 0, 1)), (x, 0, 1))

# Crear una malla de puntos para graficar la función
X = np.linspace(0, 1, 30)
Y = np.linspace(0, 1, 30)
X, Y = np.meshgrid(X, Y)
Z = X  # f(x,y) = x

# Graficar la superficie
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='k', alpha=0.7)

# Etiquetas
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('f(x,y)')
ax.set_title(f'Integral doble de f(x,y) = x sobre la región dada\nResultado: {integral_result.evalf()}')

plt.show()

# Resultado simbólico de la integral
integral_result
