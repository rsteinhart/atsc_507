# %% [markdown]
# Rachel Steinhart  
# ATSC 507 - HW7 - Dr. Roland Stull  
# March 23rd, 2020

# %%
import numpy as np
import matplotlib.pyplot as plt
# %%
# initial conditions
imax = int(1000) # number of grid points in x-direction
delx = 100 # horizontal grid spacing (m)
delt = 10 # time increment (s)
u = 5 # horizontal wind speed (m/s)

x = np.zeros(imax)
x[0:1000] = np.linspace(0,1000,1000)
# x = x.astype(int)
#x = x[0:1000]
# %%
# 1) Calculate and display the Courant number
Cr = u*delt/delx
print('The Courant number is:', Cr)

# %%
# 2a) Create initial concentration anomaly distribution in the x-direction
#conc = 0 # initial concentration of background is zero
conc = np.zeros(imax)
cmax = 10.0 # max initial concentration
conc[100:150] = np.linspace(0,cmax,50)
conc[150:200] = np.linspace(cmax,0,50)
conc[20:40] = np.linspace(0, -0.5*cmax,20)
conc[40:60] = np.linspace(-0.5*cmax,0,20)

# %%
# 3) On the same plot, show (in red) the ideal exact final solution
cideal = np.zeros(imax) # background concentration
cideal[800:850] = np.linspace(0,cmax,50)
cideal[850:900] = np.linspace(cmax,0,50)
cideal[720:740] = np.linspace(0,-0.5*cmax,20)
cideal[740:760] = np.linspace(-0.5*cmax,0,20)

# %%
# Plot
plt.plot(x,cideal, 'r')
plt.plot(x, conc, 'b')
plt.title('Part 3) Initial and Ideal concentrations')
plt.xlabel('Grid index (i)')
plt.ylabel('Concentration')
plt.show()

# %%
# 4) Advect the concentration puff anomaly for the following number of time steps 
# and plot in great the resulting concentrations using foward in time, backward in space

nsteps = (imax-300)/(u*delt/delx)
nsteps = int(nsteps)

t=[0]
time = 0
while time < nsteps-2:
    time = time+1
    t = np.append(t,time)

x1 = [1]
distance = 1
while distance < imax-1:
    distance = distance +1
    x1 = np.append(x1,distance)

s = (nsteps, imax)
Conc_ftbs = np.zeros(s)
Conc_ftbs[0,:] = conc

for n in t:
    for j in x1-1:
        Conc_ftbs[n+1,j] = -Cr*(Conc_ftbs[n,j]-Conc_ftbs[n,j-1]) + Conc_ftbs[n,j]

Conc_ftbs_plt = Conc_ftbs[-1,:]

# %%
plt.plot(x,Conc_ftbs_plt,'g')
plt.plot(x,cideal, 'r')
plt.plot(x, conc, 'b')
plt.title('Part 4) FTBS')
plt.xlabel('Grid index (i)')
plt.ylabel('Concentration')
plt.show()

# %%
# 5) Repeat steps (2-4) to re-initialize, but plotting 
# (in green) on a new graph, and using
# RK3 for the advection.  Use same number of time steps.

conc_rk3 = np.zeros(s)
term1 = np.zeros(s)
term2 = np.zeros(s)
term3 = np.zeros(s)
term4 = np.zeros(s)

conc_rk3[0,:] = conc

t5=[0]
time5 = 0
while time5 < nsteps-2:
    time5 = time5+1
    t5 = np.append(t5,time5)
#print(t5)

x5 = [3]
distance5 = 3
while distance5 < imax-1:
    distance5 = distance5 +1
    x5 = np.append(x5,distance5)
#print(x5)

for n in t5:
    for j in x5-3:
        term1 = (1-Cr*Cr/4)*conc_rk3[n,j]
        term2 = ((Cr/2)-3*(Cr*Cr*Cr/48))*(conc_rk3[n,j+1]-conc_rk3[n,j-1])
        term3 = (Cr*Cr/8)*(conc_rk3[n,j+2]+conc_rk3[n,j-2])
        term4 = (Cr*Cr*Cr/48)*(conc_rk3[n,j+3]-conc_rk3[n,j-3])

        conc_rk3[n+1,j] = term1 - term2 + term3 - term4

# %%
conc_rk3_plt = conc_rk3[-1,:]
plt.plot(x,cideal, 'r')
plt.plot(x, conc, 'b')
plt.plot(x,conc_rk3_plt,'g')
plt.title('Part 5) RK3')
plt.xlabel('Grid index (i)')
plt.ylabel('Concentration')
plt.show()

# %% [markdown]
# 7)
# The forward in time backward in space (FTSB) technique produces wider and shorter curves than the ideal solution. The transitions in concentration are also more smooth than in the ideal solution and the peaks were centered with the ideal solution. The 3rd order runga kutta (RK3) method (with second order in space) produced final concentrations with peaks that matched the ideal solution more closely than the FTSB but a small "worm" was developped. The peaks were also slightly off center from the ideal solution. Finally, the PPM scheme produced peaks that matched the ideal solution exactly. Proving that this scheme, although more computationally intensive, was most accurate for this exercise.

# %%
