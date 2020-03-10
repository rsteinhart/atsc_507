# %% [markdown]
# ATSC 507 - HW4  
# Rachel Steinhart  
# February 24th, 2020  

# %%
#Question setup
Tref_0=2
A=1
c=1.5
delta_t=1
T_ref = 2
t=0 #?

#m = t/delta_t
m=1
#t=m*delta_t

def slope(T,t):
    delT_delt = 1.5*(2-1.5*t-(T/(2-1.5*t)))
    return(delT_delt)

# %%
#Euler Forward
delT_delt = slope(T_ref, t)
T_n1 = delT_delt*delta_t + T_ref
print('Euler Forward: T at the following timestep is', T_n1)

# %%
#RK2
T_star = T_ref + (delta_t/2)*slope(T_ref, t)
T_n1_RK2 = T_ref + delta_t*slope(T_star,t+delta_t/2)
print('RK2: T at the following timestep is', T_n1_RK2)

# %%
#RK3
T_star = T_ref + (delta_t/3)*slope(T_ref,t)
T_2_star = T_ref + (delta_t/2)*slope(T_star,t+delta_t/3)
T_n1_RK3 = T_ref + delta_t*slope(T_2_star,t+delta_t/2)
print('RK3: T at the following timestep is', T_n1_RK3)

# %%
#RK4
k1 = slope(T_ref,t)
k2 = slope(T_ref+0.5*delta_t*k1,t+0.5*delta_t)
k3 = slope(T_ref+0.5*delta_t*k2,t+0.5*delta_t)
k4 = slope(T_ref + delta_t*k3,t+delta_t)
T_n1_RK4 = T_ref + (delta_t/6)*(k1 + 2*k2 + 2*k3 + k4)
print('RK4: T at the following timestep is', T_n1_RK4)

# %%
#Analytically
T_ref_3 = 3
T = A*(c*m*delta_t + T_ref_3 -Tref_0)*(Tref_0-c*m*delta_t) 
print('Analytically: T at the following timestep is', T)

# %%
# Compare results
print('Eular forward:', T_n1)
print('RK2:', T_n1_RK2)
print('RK3:', T_n1_RK3)
print('RK4:', T_n1_RK4)
print('Analytical:', T)
print('We can see that RK3 was the method that gave the closest answer to the analytical solution')


# %%
