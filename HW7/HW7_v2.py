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
plt.legend('initial','ideal')
plt.show()

# %%
# 4) Advect the concentration puff anomaly for the following number of time steps 
# and plot in great the resulting concentrations using foward in time, backward in space

nsteps = (imax-300)/(u*delt/delx)
nsteps = int(nsteps)
print(nsteps)

t=[0]
time = 0
while time < nsteps-2:
    time = time+1
    t = np.append(t,time)
print(t)

x1 = [1]
distance = 1
while distance < imax-1:
    distance = distance +1
    x1 = np.append(x1,distance)
print(x1)

s = (nsteps, imax)
Conc_ftbs = np.zeros(s)
Conc_ftbs[0,:] = conc

# for n in t:
#     for j in x1:
#         Conc_ftbs[n+1,j] = (delt/delx)*(Conc_ftbs[n,j]-Conc_ftbs[n,j-1]) + Conc_ftbs[n,j]
for n in t:
    for j in x1-1:
        Conc_ftbs[n+1,j] = -Cr*(Conc_ftbs[n,j]-Conc_ftbs[n,j-1]) + Conc_ftbs[n,j]

Conc_ftbs_plt = Conc_ftbs[-1,:]
plt.plot(x,Conc_ftbs_plt)
plt.show()





# %%
