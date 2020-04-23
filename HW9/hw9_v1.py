# %% [Markdown]
# Rachel Steinhart
# ATSC 507 HW9
# %%
import numpy as np
import matplotlib.pyplot as plt
# %%
# Q1) 
x = np.array(np.linspace(-0.9,0.9,19))
N = 3
rho = 1
k = int(len(x)/3)

area1 = x[0:k]
area2 = x[k:2*k+1]
area3 = x[2*k+1:3*k+1]

# FIX NAMINGGGG
gen_p1 = sum(area1*rho)/(1*k)
gen_p2 = sum(area2*rho)/(1*k)
gen_p3 = sum(area3*rho)/(1*k)

# %% 
# Q4)

def gnomonic_projection(R,c,proj_type):

    if proj_type == 'equidistant':
        a = (np.sqrt(3)/3)*R
        x = np.linspace(-a,a,c)
        y = np.linspace(-a,a,c)
        x_local, y_local = np.meshgrid(x,y)

    elif proj_type == 'equiangular':
        a = np.pi/4
        x0 = np.linspace(-a,a,c)
        y0 = np.linspace(-a,a,c)
        x = a*np.tan(x0)
        y = a*np.tan(y0)

        x_local, y_local = np.meshgrid(x,y)

    r = np.sqrt(a**2 + x_local**2 + y_local**2)

    Z_top = (R/r)*a
    Z_bottom = (R/r)*(-a)

    X_top = (R/r)*x_local
    X_bottom = (R/r)*(-x_local)

    Y_top = (R/r)*y_local
    Y_bottom = (R/r)*(-y_local)

    # fig = plt.figure()
    ax = plt.subplot(1,1,1, projection='3d')
    ax.plot_wireframe(X_top, Y_top, Z_top, color = 'b')
    ax.plot_wireframe(X_bottom, Y_bottom, Z_bottom, color = 'b')
    ax.plot_wireframe(Z_top, X_top, Y_top, color = 'm')
    ax.plot_wireframe(Z_bottom, X_bottom, Y_bottom, color = 'm')
    ax.plot_wireframe(X_top, Z_top, Y_top, color = 'c')
    ax.plot_wireframe(X_bottom, Z_bottom, Y_bottom, color = 'c')
    plt.title(str(c)+'c cube sphere mesh, '+proj_type+' gnomonic projection')
    plt.show()

# %%
R=2
equidistant = 'equidistant'
equiangular = 'equiangular'

gnomonic_projection(R,12,equidistant)
gnomonic_projection(R,12,equiangular)

gnomonic_projection(R,24,equidistant)
gnomonic_projection(R,24,equiangular)

gnomonic_projection(R,36,equidistant)
gnomonic_projection(R,36,equiangular)

gnomonic_projection(R,48,equidistant)
gnomonic_projection(R,48,equiangular)

# %% [Markdown]
# HOW DO THE TWO GRID PROJECTIONS COMPARE?????????????
# As the resolution of the meshes is increased the grid sizes decrease.

