# %% [markdown]
# ATSC 507 HW10  
# Rachel Steinhart  
# April 20, 2020

# %%
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
# %%
# Constants
pi = 3.14159
# %%
# Function defining polynomial
def func_y(x):
    y = 0.5*x + x*np.sin(2*pi*x/10)
    return (y)

# %%
# 1a) Plot
x_int = np.linspace(0,20,20000)
y_int = func_y(x_int)
delx = 20/20000

plt.plot(x_int, y_int)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Part 1a')
plt.show()

# 1b) Integrate
I = 0
for i in range (20000):
    I = delx*y_int[i] + I
print('Part 1b) I= ', round(I,4))

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
xi_k6= np.array([0.2386191861,-0.2386191861, 0.6612093865, -0.6612093865, 0.9324695142,-0.9324695142])
w_k6 = np.array([0.4679139346, 0.4679139346, 0.3607615730,0.3607615730,0.1713244924,0.1713244924])
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

table = {'m=2': [I2],
'm=4': [I4],
'm=6': [I6],
'm=8': [I8]}

df = pd.DataFrame(table)
print(df)

# %% [markdown]
# Gaussian quadrature reaches the exact solution for polynomials of 2n-1. We can see that for m=8, the solution agrees with the analytical solution. An increase in n/m will provide a more accurate solution because the function is fit more closely with each added point.

# %% [markdown]
# Q2) Triangular Spectral Truncation is used with highest order N=1279. 
# Meaning that there are 1280 truncation points.
# Warner has the same maximum wavenumber of 1279. 
#
# Warner's four equations are:
# $$ L_{1}= \frac{2\pi a}{3K + 1},   
# L_{2} =\frac{\pi a}{K},  L_{3}=\frac{2\sqrt{\pi}a}{K+1},
# L_{4}=\frac{\sqrt{2}\pi a}{K} $$ 
#  
# With a spectral resolution of 799 L1 = 16.7km, L2 = 25.0 km, L3 = 28.2, L4 = 35.4km
# ECMWF uses this equation:
# $$ L=\frac{2\pi a}{n} $$ 
#
# with the same spectral resolution of 799 L = 50.10km
# The ECMWF equation is most similar to L2.

# %%
# Q3a)

def find_eq(m,n,mu):
    if m==0:
        if n==1:
            deriv = 2*mu
        elif n==2:
            deriv = (12*mu**2)-4
        elif n==3:
            deriv = (120*mu**3)-72*mu
        elif n==4:
            deriv = (1680*mu**4)-(1440*mu**2)+144

    elif m==1:
        if n==1:
            deriv = 2
        elif n==2:
            deriv = 24*mu
        elif n==3:
            deriv = (360*mu**2)-72
        elif n==4:
            deriv = (6720*mu**3)-(2880*mu)
        elif n==5:
            deriv = (151200*mu**4)-(100800*mu**2)+7200
    
    elif m==2:
        if n==2:
            deriv = 24
        elif n==3:
            deriv = 720*mu
        elif n==4:
            deriv = (20160*mu**2)-2880
        elif n==5:
            deriv = (604800*mu**3)-(201600*mu)
        elif n==6:
            deriv = (19958400*mu**4)-(10886400*mu**2)+604800

    return deriv

# %%
m_a=0
n_a=np.array(np.linspace(1,4,4))
mu = np.array(np.linspace(-1,1,100))
Pmn_a = np.zeros((len(n_a),len(mu)))

for n in n_a:
    term1 = np.sqrt((2*n+1)*math.factorial(int(n-m_a))/math.factorial(int(n+m_a)))
    term2 = ((1-mu**2)**(m_a/2))/((2**n)*math.factorial(int(n)))
    term3 = find_eq(m_a,n,mu)

    P = term1*term2*term3
    Pmn_a[int(n)-1] = P

labels =['n=1','n=2','n=3','n=4']

fig, ax=plt.subplots(1,1)
plots = ax.plot(mu,Pmn_a.T)
ax.set_xlabel('mu')
ax.set_ylabel('P(mu)')
ax.legend(plots,labels)
plt.title('Q3 part a (m=0)');

# %%
# Q3b)
m_b=1
n_b=np.array(np.linspace(1,5,5))
Pmn_b = np.zeros((len(n_b),len(mu)))

for n in n_b:
    term1 = np.sqrt((2*n+1)*math.factorial(int(n-m_b))/math.factorial(int(n+m_b)))
    term2 = ((1-mu**2)**(m_b/2))/((2**n)*math.factorial(int(n)))
    term3 = find_eq(m_b,n,mu)

    P = term1*term2*term3
    Pmn_b[int(n)-1] = P
    
labels =['n=1','n=2','n=3','n=4','n=5']

fig, ax=plt.subplots(1,1)
plots = ax.plot(mu,Pmn_b.T)
ax.set_xlabel('mu')
ax.set_ylabel('P(mu)')
ax.legend(plots,labels)
plt.title('Q3 part b (m=1)');

# %%
# Q3c)
m_c=2
n_c=np.array(np.linspace(2,6,5))
Pmn_c = np.zeros((len(n_c),len(mu)))

for n in n_c:
    term1 = np.sqrt((2*n+1)*math.factorial(int(n-m_c))/math.factorial(int(n+m_c)))
    term2 = ((1-mu**2)**(m_c/2))/((2**n)*math.factorial(int(n)))
    term3 = find_eq(m_c,n,mu)

    P = term1*term2*term3
    Pmn_c[int(n)-2] = P

labels =['n=2','n=3','n=4','n=5','n=6']

fig, ax=plt.subplots(1,1)
plots = ax.plot(mu,Pmn_c.T)
ax.set_xlabel('mu')
ax.set_ylabel('P(mu)')
ax.legend(plots,labels)
plt.title('Q3 part c (m=2)');

# %%
# Q4)
# Attached
