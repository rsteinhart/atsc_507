# %% [markdown]
# ATSC 507 Homework 11  
# Rachel Steinhart  
# April 18, 2020

# %%
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

# %%
# A19
F = [5.3, 5.4, 5.5, 5.4, 5.5, 5.4, 5.5, 5.6, 5.6, 5.6, 5.6, 5.6, 5.8, 5.7, 5.6, 5.7, 5.9, 5.8, 5.7, 5.8]
F = np.array(F)

V = [5.3, 5.3, 5.3, 5.4, 5.4, 5.3, 5.4, 5.5, 5.5, 5.4, 5.5, 5.5, 5.7, 5.5, 5.6, 5.6, 5.8, 5.7, 5.6, 5.6]
V = np.array(V)

A = [5.2,5.3,5.4,5.3,5.3,5.4,5.5,5.4,5.4,5.5,5.6,5.5,5.5,5.6,5.7,5.6,5.6,5.7,5.8,5.7]
A = np.array(A)

C = [5.4,5.4,5.4,5.4,5.4,5.4,5.4,5.4,5.5,5.5,5.5,5.5,5.6,5.6,5.6,5.6,5.7,5.7,5.7,5.7]
C = np.array(C)
# %%
# a) Mean forecast error

F_ave = (F.sum(axis =0, dtype='float'))/len(F)
V_ave = (V.sum(axis =0, dtype='float'))/len(V)

ME = F_ave - V_ave
print('The mean forecast error is', ME)

# %%
# b) mean persistence error
A_ave = (A.sum(axis =0, dtype='float'))/len(A)

MPE = A_ave - V_ave
print('The mean persistence error is', MPE)

# %%
# c) mean absolute forecast error
f_v = F - V
MAE = (f_v.sum(axis =0, dtype='float'))/len(f_v)
print('The mean absolute forecast error is', MAE)
# %%
# d) mean squared forecast error
fv2 = f_v*f_v
MSE = (fv2.sum(axis =0, dtype='float'))/len(fv2)
print('The mean squared forecast error is', MSE)

# %%
# e) mean squared climatology error
cv2 = (C-V)**2
MSEC = (cv2.sum(axis =0, dtype='float'))/len(cv2)
print('The mean squared climatology error is', MSEC)

# %%
# f) mean squared forecast error skill score
MSESS = 1 - (MSE/MSEC)
print('The mean squared forecast error skill score is', MSESS)

# %%
# g) RMS forecast score
RMSEF = np.sqrt(MSE)
print('The RMS forecast score is', RMSEF)

# %%
# h) correlation coefficient between forecast and verification
F_prime = F - F_ave
V_prime = V - V_ave
fv_prime = F_prime*V_prime
fv_ave = (fv_prime.sum(axis=0,dtype='float'))/len(fv_prime)

rc = (fv_ave)/(np.sqrt((F_prime**2).sum(axis=0,dtype='float')/len(F))*np.sqrt((V_prime**2)).sum(axis=0,dtype='float')/len(F))
print('The correlation coefficient is', rc)

# %%
# i) forecast anomoly correlation
term1 = (F-C)-((F-C).sum(axis=0,dtype='float')/len(F))
term2 = (V-C)-((V-C).sum(axis=0,dtype='float')/len(V))
term3 = term1**2
term4 = term2**2
numerator = (term1*term2).sum(axis=0,dtype='float')/len(F)
denominator = np.sqrt((term3*term4).sum(axis=0,dtype='float')/len(F))

FAC = numerator/denominator
print('The forecast anomoly correlation is', FAC)

# %%
# j) persistence anomaly correlation
term1 = (A-C)-((A-C).sum(axis=0,dtype='float')/len(F))
term2 = (V-C)-((V-C).sum(axis=0,dtype='float')/len(V))
term3 = term1**2
term4 = term2**2
numerator = (term1*term2).sum(axis=0,dtype='float')/len(F)
denominator = np.sqrt((term3*term4).sum(axis=0,dtype='float')/len(F))

PAC = numerator/denominator
print('The persistance anomoly correlation is', PAC)

# k) draw height contours by hand 
# attached

# %%
# A20
a = 150
b = 65
c = 50
d = 100
n = 365

B = (a+b)/(a+c)
print('The bias score is', B)
PC = (a+b)/n
print('The portion correct is', PC)
E = ((a+b)/n)*((a+c)/n) + ((d+b)/n)*((d+c)/n)
print('The random luck ratio is', E)
HSS = (PC-E)/(1-E)
print('The Heidke skill score is', HSS)
H = a/(a+c)
print('The hit rate is', H)
F = b/(b+d)
print('The false alarm rate is',F)
FAR = b/(a+b)
print('The false-alarm ratio', FAR)
TSS = H-F
print('The true skill score is', TSS)
CSI = a/(a+b+c)
print('The critical success index is',CSI)
ar = (((a+b)*(a+c))/n)
print('The portion of random hits is',ar)
GSS = (a-ar)/(a-ar+b+c)
print('The Gilberts skill score is',GSS)

# %%
# A21
cost = 5 #thousand dollars
loss = 50 #thousand dollars
o = 0.5

E_climate = np.minimum(cost,o*loss)
E_fcst = a*cost/n + b*cost/n + c*loss/n
E_perfect = o*cost

V = (E_climate-E_fcst)/(E_climate-E_perfect)
print('The forecast value is', V)

# %%
# A22
k = np.linspace(0,20,21)
k = np.array(k)
pk = [0.9,0.85,0.8,0.75,0.7,0.65,0.6,0.55,0.5,0.45,0.4,0.35,0.3,0.25,0.2,0.15,0.1,0.05,0.02,0]
pk = np.array(pk)
ok = [1,1,0,1,1,1,0,1,0,1,0,0,1,0,0,1,0,0,0,0]
ok = np.array(ok)

# Brier Skill Score
num = ((pk-ok)**2).sum(axis=0,dtype='float')
den_1 = ok.sum(axis=0,dtype='float')
den_2 = len(k)- den_1

BSS = 1 - num/(den_1*den_2)
print('The Brier Skill Score is', BSS)

# Probability bins of width delp=0.2
delp=0.2
pj = np.array([0.2,0.4,0.6,0.8,1.0])
j = np.array([0,1,2,3,4,5])
nj = np.array([4,4,4,4,4])
noj = np.array([3,3,1,2,0])
ratio = noj/nj

plt.plot(pj,ratio)
plt.title('Reliability Diagram')
plt.xlabel('Probability')
plt.ylabel('Ratio')
plt.show()
# Relative reliability 
num = (((nj*pj)-noj)**2).sum(axis=0,dtype='float')

BSS_reliability = num/(den_1*den_2)
print('The Reliability Brier Skill Score is', BSS_reliability)

# %%
# A23
# 10-member ensemble forecast, probabilites that 24h acc precip >5mm
# calc hit rate, false alarm rate for the full range of 
# allowed probability theshold and plot the result as a ROC diagram 
# find the area under the ROC curve and find the ROC skill score
day = np.array(np.linspace(1,30,30))
o = np.array([1,0,1,1,0,0,0,1,0,1,1,0,0,0,1,0,1,1,1,0,0,0,0,0,1,0,0,1,0,1])
p = np.array([50,20,20,60,50,20,30,90,40,30,100,10,0,10,80,60,70,90,80,70,10,10,0,0,80,0,0,100,10,90])
zero = np.array([1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,0,0,1,0,0,1,1,1])
ten = np.array([1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,0,0,1,0,0,1,1,1])
twenty = np.array([1,0,0,1,1,0,1,1,1,1,1,0,0,0,1,1,1,1,1,1,0,0,0,0,1,0,0,1,0,1])
thirty = np.array([1,0,0,1,1,0,1,1,1,1,1,0,0,0,1,1,1,1,1,1,0,0,0,0,1,0,0,1,0,1])
fourty = np.array([1,0,0,1,1,0,0,1,1,0,1,0,0,0,1,1,1,1,1,1,0,0,0,0,1,0,0,1,0,1])
fifty = np.array([1,0,0,1,1,0,0,1,0,0,1,0,0,0,1,1,1,1,1,1,0,0,0,0,1,0,0,1,0,1])
sixty = np.array([0,0,0,1,0,0,0,1,0,0,1,0,0,0,1,1,1,1,1,1,0,0,0,0,1,0,0,1,0,1])
seventy = np.array([0,0,0,0,0,0,0,1,0,0,1,0,0,0,1,0,1,1,1,1,0,0,0,0,1,0,0,1,0,1])
eighty = np.array([0,0,0,0,0,0,0,1,0,0,1,0,0,0,1,0,0,1,1,0,0,0,0,0,1,0,0,1,0,1])
ninety = np.array([0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,1])
hundred = np.array([0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0])

# Calculate a,b,c,d for each probability
a0 = np.zeros(len(day))
b0 = np.zeros(len(day))
c0 = np.zeros(len(day))
d0 = np.zeros(len(day))

for i in range(len(day)):
    if o[i]==1 and zero[i]==1:
        a0[i]=1
    if o[i]==0 and zero[i]==1:
        b0[i]=1
    if o[i]==1 and zero[i]==0:
        c0[i]=1
    if o[i]==0 and zero[i]==0:
        d0[i]=1

a10 = np.zeros(len(day))
b10 = np.zeros(len(day))
c10 = np.zeros(len(day))
d10 = np.zeros(len(day))

for i in range(len(day)):
    if o[i]==1 and ten[i]==1:
        a10[i]=1
    if o[i]==0 and ten[i]==1:
        b10[i]=1
    if o[i]==1 and ten[i]==0:
        c10[i]=1
    if o[i]==0 and ten[i]==0:
        d10[i]=1

a20 = np.zeros(len(day))
b20 = np.zeros(len(day))
c20 = np.zeros(len(day))
d20 = np.zeros(len(day))

for i in range(len(day)):
    if o[i]==1 and twenty[i]==1:
        a20[i]=1
    if o[i]==0 and twenty[i]==1:
        b20[i]=1
    if o[i]==1 and twenty[i]==0:
        c20[i]=1
    if o[i]==0 and twenty[i]==0:
        d20[i]=1

a30 = np.zeros(len(day))
b30 = np.zeros(len(day))
c30 = np.zeros(len(day))
d30 = np.zeros(len(day))

for i in range(len(day)):
    if o[i]==1 and thirty[i]==1:
        a30[i]=1
    if o[i]==0 and thirty[i]==1:
        b30[i]=1
    if o[i]==1 and thirty[i]==0:
        c30[i]=1
    if o[i]==0 and thirty[i]==0:
        d30[i]=1

a40 = np.zeros(len(day))
b40 = np.zeros(len(day))
c40 = np.zeros(len(day))
d40 = np.zeros(len(day))

for i in range(len(day)):
    if o[i]==1 and fourty[i]==1:
        a40[i]=1
    if o[i]==0 and fourty[i]==1:
        b40[i]=1
    if o[i]==1 and fourty[i]==0:
        c40[i]=1
    if o[i]==0 and fourty[i]==0:
        d40[i]=1

a50 = np.zeros(len(day))
b50 = np.zeros(len(day))
c50 = np.zeros(len(day))
d50 = np.zeros(len(day))

for i in range(len(day)):
    if o[i]==1 and fifty[i]==1:
        a50[i]=1
    if o[i]==0 and fifty[i]==1:
        b50[i]=1
    if o[i]==1 and fifty[i]==0:
        c50[i]=1
    if o[i]==0 and fifty[i]==0:
        d50[i]=1

a60 = np.zeros(len(day))
b60 = np.zeros(len(day))
c60 = np.zeros(len(day))
d60 = np.zeros(len(day))

for i in range(len(day)):
    if o[i]==1 and sixty[i]==1:
        a60[i]=1
    if o[i]==0 and sixty[i]==1:
        b60[i]=1
    if o[i]==1 and sixty[i]==0:
        c60[i]=1
    if o[i]==0 and sixty[i]==0:
        d60[i]=1

a70 = np.zeros(len(day))
b70 = np.zeros(len(day))
c70 = np.zeros(len(day))
d70 = np.zeros(len(day))

for i in range(len(day)):
    if o[i]==1 and seventy[i]==1:
        a70[i]=1
    if o[i]==0 and seventy[i]==1:
        b70[i]=1
    if o[i]==1 and seventy[i]==0:
        c70[i]=1
    if o[i]==0 and seventy[i]==0:
        d70[i]=1

a80 = np.zeros(len(day))
b80 = np.zeros(len(day))
c80 = np.zeros(len(day))
d80 = np.zeros(len(day))

for i in range(len(day)):
    if o[i]==1 and eighty[i]==1:
        a80[i]=1
    if o[i]==0 and eighty[i]==1:
        b80[i]=1
    if o[i]==1 and eighty[i]==0:
        c80[i]=1
    if o[i]==0 and eighty[i]==0:
        d80[i]=1

a90 = np.zeros(len(day))
b90 = np.zeros(len(day))
c90 = np.zeros(len(day))
d90 = np.zeros(len(day))

for i in range(len(day)):
    if o[i]==1 and ninety[i]==1:
        a90[i]=1
    if o[i]==0 and ninety[i]==1:
        b90[i]=1
    if o[i]==1 and ninety[i]==0:
        c90[i]=1
    if o[i]==0 and ninety[i]==0:
        d90[i]=1

a100 = np.zeros(len(day))
b100 = np.zeros(len(day))
c100 = np.zeros(len(day))
d100 = np.zeros(len(day))

for i in range(len(day)):
    if o[i]==1 and hundred[i]==1:
        a100[i]=1
    if o[i]==0 and hundred[i]==1:
        b100[i]=1
    if o[i]==1 and hundred[i]==0:
        c100[i]=1
    if o[i]==0 and hundred[i]==0:
        d100[i]=1

hit_rate = np.zeros(11)
false_alarm = np.zeros(11)

a = np.array([np.sum(a0), np.sum(a10), np.sum(a20), np.sum(a30), np.sum(a40), np.sum(a50), np.sum(a60), np.sum(a70), np.sum(a80), np.sum(a90), np.sum(a100)])
b = np.array([np.sum(b0), np.sum(b10), np.sum(b20), np.sum(b30), np.sum(b40), np.sum(b50), np.sum(b60), np.sum(b70), np.sum(b80), np.sum(b90), np.sum(b100)])
c = np.array([np.sum(c0), np.sum(c10), np.sum(c20), np.sum(c30), np.sum(c40), np.sum(c50), np.sum(c60), np.sum(c70), np.sum(c80), np.sum(c90), np.sum(c100)])
d = np.array([np.sum(d0), np.sum(d10), np.sum(d20), np.sum(d30), np.sum(d40), np.sum(d50), np.sum(d60), np.sum(d70), np.sum(d80), np.sum(d90), np.sum(d100)])

# Calculate hit rate and false alarm rate
for i in range(11):
    hit_rate[i] = a[i]/(a[i]+c[i])
    false_alarm[i] = b[i]/(b[i]+d[i])

hit_rate = np.nan_to_num(hit_rate)
hit_rate = np.array(np.sort(hit_rate))
false_alarm = np.nan_to_num(false_alarm)
false_alarm = np.array(np.sort(false_alarm))


print('Hit rate =',hit_rate)
print('False alarm rate = ',false_alarm)

plt.plot(false_alarm,hit_rate,'o')
plt.title('ROC plot')
plt.xlabel('False Alarm Rate')
plt.ylabel('Hit Rate')
plt.show()

# Compute the area using the Trapezoid rule
area = np.trapz(hit_rate, x=false_alarm)
print("area =", area)
