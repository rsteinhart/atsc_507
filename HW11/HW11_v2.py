# %%
import numpy as np
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
# ????????????
# ????????????
# ????????????
# ????????????
# ????????????
# ????????????
# ????????????

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
ar = ((a+b)*(a+c)/n)
print('The portion of random hits is',ar)
GSS = (a-ar)/(a-ar+b+c)
print('The Gilberts skill score is',GSS)

# %%
# A21
cost = 5 #thousand dollars
loss = 50 #thousand dollars
o = 0.5

E_climate = np.min(cost,o*loss)
E_fcst = a*coss/n + b*cost/n + c*loss/n
E_perfect = o*Cost

V = (E_climate-E_fcst)/(E_climate-E_perfect)
print('The forecast value is', V)

# %%
# A22
k = np.linspace(0,20,21)
pk = [0.9,0.85,0.8,0.75,0.7,0.65,0.6,0.55,0.5,0.45,0.4,0.35,0.3,0.25,0.2,0.15,0.1,0.05,0.02,0]
ok = [1,1,0,1,1,1,0,1,0,1,0,0,1,0,0,1,0,0,0,0]
