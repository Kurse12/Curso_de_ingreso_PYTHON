import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # Importa Axes3D para gráficos 3D
from matplotlib import cm
from matplotlib import animation
from IPython.display import HTML

# Definir la función que genera la superficie de la flor
def superficie_flor():
    x, t = np.meshgrid(np.array(range(25))/24,
                       np.pi * (np.arange(0, 575, 0.5)/575*17 - 2))
    p = (np.pi/2) * np.exp(-t/(8 * np.pi))
    u = (1 - np.mod(3.6 * t, 2 * np.pi) / np.pi)**4 / 2
    y = 2 * (x**2 - x)**2 * np.sin(p)
    r = u * (x * np.sin(p) + y * np.cos(p))
    return r * np.cos(t), r * np.sin(t), u * (x * np.cos(p) - y * np.sin(p))

# Crear la figura y el eje
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10, 18))  # Crear una figura con tamaño (ancho, alto)

ax = fig.add_subplot(111, projection='3d')  # Añadir un subplot tridimensional

# Configurar el color de fondo de la figura
ax.set_facecolor('black')

# Desactivar el relleno del plano XY, YZ y ZX
ax.xaxis.pane.fill = False
ax.yaxis.pane.fill = False
ax.zaxis.pane.fill = False

X, Y, Z =superficie_flor()
surf= ax.plot_surface(X,Y,Z, rstride=1, cstride = 1,cmap=cm.gist_rainbow_r, linewidth = 0,antialiased = True)

def animate(i):
    ax.view_init(elev=10., azim=i)
    return surf,  # Devolvemos una tupla con el objeto surf, la coma al final es importante

anim = animation.FuncAnimation(fig, animate, frames=360, interval=20, blit=True)




anim.save("sandreke_3Dflower.mp4", fps=30)


HTML(anim.to_html5_video())