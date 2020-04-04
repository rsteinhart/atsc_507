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

xk = (b+a)/2 + ((b-a)/2)*Gammak
sum_m = 0

for i = 1:n:
    sum_m = wk*func_y(xk) + sum_m

integral_ab = ((b-a)/2)*sum_m

