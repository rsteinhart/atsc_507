# %% 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from math import gamma 
# %%
# Constants
pi = 3.14159
# x = np.linspace(0,20,20)

# %%
def func_y(x):
    y = 0.5*x + x*np.sin(2*pi*x/10)
    return (y)

# %%
# 1a) Plot
# y = func_y(x)
# plt.plot(x,y)
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('Part 1a')
# plt.show()

# %%
# 1b) Integrate
x_int = np.linspace(0,20,20000)
y_int = func_y(x_int)
delx = 20/20000

plt.plot(x_int, y_int)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Part 1a')
plt.show()

I = 0
for i in range (20000):
    I = delx*y_int[i] + I
print('Part 1b) I=',I)

# %%
# 1b) Plot
# plt.plot(x_int, y_int)
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('Part 1b')
# plt.show()

# %%
# functions
def calc_xk(a,b,xi_k):
    xk = (b+a)/2 + ((b-a)/2)*xi_k
    return xk

def Gauss_int(a,b,wk,fxk):
    I = ((b-a)/2)*sum(w_k*fxk)
    return I
# %%
# 1c) Gaussian quadrature
a = 0
b = 20

m = 2
xi_k2 = np.array([0.5773502692,-0.5773502692])
w_k2 = np.array([1,1])
xk2 = (b+a)/2 + ((b-a)/2)*xi_k2
fxk2 = func_y(xk2)
I2 = ((b-a)/2)*sum(w_k2*fxk2)
# print(I2)

m = 4
xi_k4 = np.array([0.3399810436,-0.3399810436, 0.8611363116, -0.8611363116])
w_k4 = np.array([0.6521451549, 0.6521451549, 0.3478548451,0.3478548451])
xk4 = calc_xk(a,b,xi_k4)
fxk4 = func_y(xk4)
I4 = ((b-a)/2)*sum(w_k4*fxk4)
# print(I4)

m = 6
xi_k6= np.array([0.3399810436,-0.3399810436, 0.8611363116, -0.8611363116])
w_k6 = np.array([0.6521451549, 0.6521451549, 0.3478548451,0.3478548451])
xk6 = calc_xk(a,b,xi_k6)
fxk6 = func_y(xk6)
I6 = ((b-a)/2)*sum(w_k6*fxk6)
# print(I6)

m = 8
xi_k8= np.array([0.1834346425,-0.1834346425,0.5255324099,-0.5255324099, 0.7966664774,-0.7966664774, 0.9602898565,-0.9602898565])
w_k8 = np.array([0.3626837834,0.3626837834,0.3137066459,0.3137066459, 0.2223810345,0.2223810345, 0.1012285362,0.1012285362])
xk8 = calc_xk(a,b,xi_k8)
fxk8 = func_y(xk8)
I8 = ((b-a)/2)*sum(w_k8*fxk8)
# print(I8)

table = {'m=2 I': [I2],
'm=4 I': [I4],
'm=6 I': [I6],
'm=8 I': [I8]}

df = pd.DataFrame(table)
print(df)

# %%
# Gaussian quadrature reaches the exact solution for polynomials of 2n-1. We can see that 
# for m=8, the solution agrees with the analytical solution.
# ?????????


# %%
#Q2) Triangular Spectral Truncation is used with N=399
# whereas Warner uses resultion of 799
# file:///C:/Users/Rachel%20Steinhart/Downloads/10125-ensemble-data-assimilations-ecmwf.pdf
# 
# %% 
# Q3a)
m=0
n=np.array(np.linspace(0,4,5))
d = 0.5 #??
mu = np.array(np.linspace(-1,1,10))

def calc_P(m,n,mu,d):
    term1 = np.sqrt((2*n+1)*gamma(int(n-m+1))/gamma(int(n+m+1)))
    term2 = ((1-mu**2)**(m/2))/((2**n)*gamma(int(n+1)))
    term3 = (d**(n+m))/(d*mu**(n+m))
    term4 = (mu**2 - 1)**n

    P = term1*term2*term3*term4
    return P

P_matrix = np.zeros((len(n),len(mu)))
i=0
for elem in n:
    P_matrix[i,:] = calc_P(m,elem,mu,d)
    i=i+1

for i in range(len(n)):
    plt.plot(mu,P_matrix[i,:])
plt.show()

# %%
# Q3b)
m=1
n=np.array(np.linspace(1,5,5))
d = 0.5 #??
mu = np.array(np.linspace(-1,1,10))

P_matrix = np.zeros((len(n),len(mu)))
i=0
for elem in n:
    P_matrix[i,:] = calc_P(m,elem,mu,d)
    i=i+1

for i in range(len(n)):
    plt.plot(mu,P_matrix[i,:])
plt.show()

# %%
# Q3c)
m=2
n=np.array(np.linspace(2,6,5))
d = 0.5 #??
mu = np.array(np.linspace(-1,1,10))

P_matrix = np.zeros((len(n),len(mu)))
i=0
for elem in n:
    P_matrix[i,:] = calc_P(m,elem,mu,d)
    i=i+1

for i in range(len(n)):
    plt.plot(mu,P_matrix[i,:])
plt.show()

# %%
# Q4)
