import numpy as np
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm


fname = "spule_ohnepanel.txt"
fname2 = "spule_panel_inX_degauss.txt"

dataO = np.loadtxt(str(fname))
zO = np.split(dataO, 7)
dataM = np.loadtxt(str(fname))
zM = np.split(dataM, 7)

x = np.arange(7)
y = np.arange(7)
X, Y = np.meshgrid(x,y)

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot_surface(X,Y,zO, rstride=1, cstride=1, alpha = 0.5, cmap='rainbow')
ax.plot_surface(X,Y,zM, rstride=1, cstride=1, alpha = 0.5, cmap='rainbow')
plt.show()
