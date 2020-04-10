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
