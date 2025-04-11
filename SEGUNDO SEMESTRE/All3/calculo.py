import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator

# Crear la figura y los ejes 3D
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

# Crear las mallas de los ejes X y Y
x = np.arange(-8, 8, 1)
y = np.arange(-8, 8, 1)
x, y = np.meshgrid(x, y)

# Calcular los valores Z
z = (x**2 + y**2)
z1 = (4*x + 8*y-20)
# Crear la superficie 3D

xs=[2]
ys=[4]
zs=[20]
colors= 'r'

ax.scatter(xs,ys,zs, c=colors, s=150)

surf = ax.plot_surface(x, y, z, edgecolor='royalblue' , lw=0.5,rstride=2,cstride=2,alpha=0.3)
surf = ax.plot_surface(x,y,z1,cmap=cm.coolwarm,alpha=0.6)

# Añadir la barra de color
ax.set_xlabel('Eje x')
ax.set_ylabel('Eje y')
ax.set_zlabel('Eje z')

# Mostrar el gráfico
plt.show()
