import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import AxesGrid

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("comp", help = "b field component to be plotted, Bx, By, Bz or normB")
args = parser.parse_args()

"""
Data
"""
old = []
with open("newcoils", "r") as f:
    for line in f:
        old.append(line.split())
old.pop(0)

bxo = np.asarray([float(i[3]) for i in old])
byo = np.asarray([float(i[4]) for i in old])
bzo = np.asarray([float(i[6]) for i in old])

xoff = 19.88
zoff = 16.95

Bx = bxo + xoff
By = byo - zoff
Bz = bzo - xoff

normB = np.sqrt(Bx**2 + By**2 + Bz**2)

"""
Plots
"""
comp = args.comp

lb = np.min(eval(comp)) - 0.1*np.abs(np.min(eval(comp)))
ub = np.max(eval(comp)) + 0.1*np.abs(np.max(eval(comp)))

fig = plt.figure(1, (11.,4.5))

grid = AxesGrid(fig, 111,
        nrows_ncols = (1,3),
        label_mode = "L",
        axes_pad = 0.2,
        share_all = False,
        cbar_location="right",
        cbar_mode = "single",
        cbar_size = "7%",
        cbar_pad = "5%",
        )

grid[1].set_xlabel("x")
grid[0].set_ylabel("y")

im = grid[0].imshow(eval(comp).reshape(3,6,6)[0], origin = 'lower', vmin=lb, vmax=ub)
im.set_interpolation('none')
grid[0].set_title("z=-35cm")
cbar = grid.cbar_axes[0].colorbar(im)
cbar.ax.get_yaxis().labelpad=10
cbar.ax.set_ylabel("nT", rotation=90)

im = grid[1].imshow(eval(comp).reshape(3,6,6)[1], origin = 'lower', vmin=lb, vmax=ub)
im.set_interpolation('none')
grid[1].set_title("z=0cm")
grid.cbar_axes[1].colorbar(im)

im = grid[2].imshow(eval(comp).reshape(3,6,6)[2], origin = 'lower', vmin=lb, vmax=ub)
im.set_interpolation('none')
grid[2].set_title("z=35cm")
#grid.cbar_axes[2].colorbar(im)
#for cax in grid.cbar_axes:
#    cax.toggle_label(False)

fig.suptitle("new coils, {}".format(comp), fontsize=18)
fig.subplots_adjust(left=0.05, right=0.95)
fig.savefig("new_{}".format(comp)+".png", dpi=300, bbox_inches = 'tight')
#plt.draw()
#plt.show()
