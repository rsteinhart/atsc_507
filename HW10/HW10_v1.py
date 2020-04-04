# %% 
import numpy as np
import matplotlib.pyplot as plt
# %%
# Constants
pi = 3.14159
x = np.linspace(0,20,20)

# %%
def func_y(x):
    y = 0.5*x + x*np.sin(2*pi*x/10)
    return (y)

# %%
# 1a) Plot
y = func_y(x)
plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Part 1a')
plt.show()

# %%
# 1b) Integrate
x_int = np.linspace(0,20,20000)
y_int = func_y(x_int)
delx = 20/20000

I = 0
for i in range (20000):
    I = delx*y_int[i] + I
print('Part 1b) I=',I)

# %%
# 1b) Plot
plt.plot(x_int, y_int)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Part 1b')
plt.show()

# %%
# 1c) Gaussian quadrature

# i) n = 2
n_i = 2
Gammak_i = 0.5773502692
wk_i = 1
a = 0 #?
b = pi/2 #?

xk_i = [(b+a)/2 + ((b-a)/2)*Gammak_i,(b+a)/2 + ((b-a)/2)*(-1)*Gammak_i]
sum_m = 0

for i in range(n_i):
    sum_m = wk_i*func_y(xk_i[i]) + sum_m

integral_ab = ((b-a)/2)*sum_m
print('Part 1ci) I = ',integral_ab)

# %%
# 1c) Gaussian quadrature TAKE 2

# i) n = 2
n = [2,4,6,8]
Gammak_i = [[0.5773502692],
            [0.3399810436, 0.8611363116],
            [0.2386191861,0.6612093865,0.9324695142],
            [0.1834346425,0.5255324099, 0.7966664774, 0.9602898565]]

wk_i = [[1],
        [0.6521451549, 0.3478548451],
        [0.4679139346, 0.3607615730, 0.1713244924],
        [0.3626837834, 0.3137066459, 0.2223810345, 0.1012285362]]

a = 0 #?
b = pi/2 #?


sum_m = 0

for i in range(length(n)):
    for j in range(n(i)/2):
        xk[i,j] = [(b+a)/2 + ((b-a)/2)*Gammak_i[i,j],(b+a)/2 + ((b-a)/2)*(-1)*Gammak_i[i,j]]

for i in range(length(n)):
    for j in range(n(i)/2):        
        sum_m = wk_i*func_y(xk[i,j]) + sum_m
        

integral_ab = ((b-a)/2)*sum_m
print(integral_ab)

