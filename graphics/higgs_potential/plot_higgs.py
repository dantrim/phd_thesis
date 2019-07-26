from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot as plt
from matplotlib import cm
import numpy as np


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create the mesh in polar coordinates and compute corresponding Z.
r = np.linspace(0, 0.93, 50)
p = np.linspace(0, 2*np.pi, 50)
R, P = np.meshgrid(r, p)
#Z = ((R**2 - 1)**2)
mu = -1
lam = 0.9
Z = 1 * (mu * R**2 + lam * R**4)

# Express the mesh in the cartesian system.
X, Y = R*np.cos(P), R*np.sin(P)
#X+=0.5
#Y-=0.5
Z+=0.5

# Plot the surface.
#ax.plot_surface(X, Y, Z, cmap=plt.cm.YlGnBu_r, alpha = 0.5)
#ax.plot_surface(X, Y, Z, cmap="coolwarm", alpha = 0.5, linewidth = 1,
ax.plot_surface(X, Y, Z, cmap="binary",  alpha = 0.5, linewidth = 0.75,
	edgecolor = "k")
ax.plot([0.1, 0.2], [0.1,0.2], color = "r", linewidth = 2, zdir="y", zs = 1)

# Tweak the limits and add latex math labels.
#ax.set_zlim(0, 1)
#ax.set_xlim(-,40)
#ax.set_ylim(-,40)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_xticklabels([])
ax.set_yticklabels([])
ax.set_zticklabels([])
#ax.set_xlabel(r'$\phi_\mathrm{real}$')
#ax.set_ylabel(r'$\phi_\mathrm{im}$')
ax.set_zlabel(r'$V(\phi)$')

plt.show()
