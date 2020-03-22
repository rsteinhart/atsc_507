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
plt.plot(x,Conc_ftbs_plt,'g')
plt.plot(x,cideal, 'r')
plt.plot(x, conc, 'b')
plt.legend('initial','ideal')
plt.title('Final plot for part 4')
plt.show()

# %%
# 5) Repeat steps (2-4) to re-initialize, but plotting 
# (in green) on a new graph, and using
# RK3 for the advection.  Use same number of time steps.

##################################           OLD         #############################

# def slope(C_ref,C_ref_1,x):
#     delC_delx = (C_ref_1-C_ref)/dx
#     return(delC_delx)

# def RK3(Tref,delta_t):
#     T_star = T_ref + (delta_t/3)*slope(T_ref,t)
#     T_2_star = T_ref + (delta_t/2)*slope(T_star,t+delta_t/3)
#     T_n1_RK3 = T_ref + delta_t*slope(T_2_star,t+delta_t/2)
#     print('RK3: T at the following timestep is', T_n1_RK3)
#     return(T_n1_RK3)
# dx = 1

# for n in t:
#     for j in x1-1:
#         slope = slope(conc[n,j],conc[n,j+1],dx)
#         conc_star = conc[n,j] + (delt/3)*slope(conc[n,j],conc[n,j+1],dx)
#         conc_2_star = conc[n,j] + (delt,2)*slope(conc_star,conc[n,j+1],dx)
#         conc_n1 = 

#####################################################################################

#T_tendency_j = – (1/2) * Cr * [T(j+1) - T(j) ] + (Cr*Cr/8) * [ T(j+2) - 2 T(j) + T(j-2) ] - (Cr*Cr*Cr/48) * [ T(j+3) - 3T(j+1) + 3T(j-1) - T(j-3) ]
conc_j_n = np.zeros(s)
term1 = np.zeros(s)
term2 = np.zeros(s)
term3 = np.zeros(s)
conc_tendency_j = np.zeros(s)

conc_j_n[0,:] = conc

t5=[1]
time5 = 1
while time5 < nsteps-2:
    time5 = time5+1
    t5 = np.append(t5,time5)
print(t5)

x5 = [4]
distance5 = 4
while distance5 < imax-1:
    distance5 = distance5 +1
    x5 = np.append(x5,distance5)
print(x5)

for n in t5:
    for j in x5-3:
        term1[n,j] = -1*(1/2)*Cr*(conc_j_n[n,j+1] - conc_j_n[n,j])
        term2[n,j] = (Cr*Cr/8)*(conc_j_n[n,j+2] -2*conc_j_n[n,j] + conc_j_n[n,j-2])
        term3[n,j] = (Cr*Cr*Cr/48)*(conc_j_n[n,j+3] - 3*conc_j_n[n,j+1] + 3*conc_j_n[n,j-1] - conc_j_n[n,j-3])

        conc_tendency_j[n,j] = term1[n,j] + term2[n,j] + term3[n,j]
        conc_j_n[n,j+1] = conc_j_n[n,j] + conc_tendency_j[n,j]

# %%
conc_j_n_plt = conc_j_n[-1,:]
plt.plot(x,conc_j_n_plt)
plt.show()

# %%
print(conc_j_n[0,:])
print(conc)
print(t)

