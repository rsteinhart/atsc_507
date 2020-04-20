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

# %%
#Q2) Triangular Spectral Truncation is used with highest order N=1279
# whereas Warner uses resultion of 799

# %% 
# Q3a)

# def calc_P(m,n,mu):
#     term1 = np.sqrt((2*n+1)*gamma(int(n-m+1))/gamma(int(n+m+1)))
#     term2 = ((1-mu**2)**(m/2))/((2**n)*gamma(int(n+1)))
#     term3 = (d**(n+m))/(d*mu**(n+m))
#     term4 = find_eq(m,n,mu)

#     P = term1*term2*term3*term4
#     return P

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
    # Pmn = calc_P(m_a,elem,mu)
    term1 = np.sqrt((2*+1)*math.factorial(int(n-m_a))/math.factorial(int(n+m_a)))
    term2 = ((1-mu**2)**(m/2))/((2**n)*math.factorial(int(n)))
    term3 = find_eq(m_a,n,mu)

    P = term1*term2*term3
    Pmn_a[int(n)-1] = P

labels =['n=1','n=2','n=3','n=4']

fig, ax=plt.subplots(1,1)
plots = ax.plot(mu,Pmn_a.T)
ax.set_xlabel('mu')
ax.set_ylabel('P(mu)')
ax.legend(plots,labels)
plt.title('Q3 part a (m=0)')

# %%
# Q3b)
m_b=1
n_b=np.array(np.linspace(1,5,5))
Pmn_b = np.zeros((len(n_b),len(mu)))

for n in n_b:
    # Pmn = calc_P(m_a,elem,mu)
    term1 = np.sqrt((2*+1)*math.factorial(int(n-m_b))/math.factorial(int(n+m_b)))
    term2 = ((1-mu**2)**(m/2))/((2**n)*math.factorial(int(n)))
    term3 = find_eq(m_b,n,mu)

    P = term1*term2*term3
    Pmn_b[int(n)-1] = P
labels =['n=1','n=2','n=3','n=4','n=5']

fig, ax=plt.subplots(1,1)
plots = ax.plot(mu,Pmn_b.T)
ax.set_xlabel('mu')
ax.set_ylabel('P(mu)')
ax.legend(plots,labels)
plt.title('Q3 part b (m=1)')

# %%
# Q3c)
m_c=2
n_c=np.array(np.linspace(2,6,5))
Pmn_c = np.zeros((len(n_c),len(mu)))

for n in n_c:
    term1 = np.sqrt((2*+1)*math.factorial(int(n-m_c))/math.factorial(int(n+m_c)))
    term2 = ((1-mu**2)**(m/2))/((2**n)*math.factorial(int(n)))
    term3 = find_eq(m_c,n,mu)

    P = term1*term2*term3
    Pmn_c[int(n)-2] = P

labels =['n=2','n=3','n=4','n=5','n=6']

fig, ax=plt.subplots(1,1)
plots = ax.plot(mu,Pmn_c.T)
ax.set_xlabel('mu')
ax.set_ylabel('P(mu)')
ax.legend(plots,labels)
plt.title('Q3 part c (m=2)')

# %%
# Q4)
# Attached