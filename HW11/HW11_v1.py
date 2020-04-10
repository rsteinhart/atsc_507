# %%
import numpy as np
# %% 
# A19
# F = [[5.3, 5.4, 5.5, 5.4],
#     [5.5, 5.4, 5.5, 5.6],
#     [5.6, 5.6, 5.6, 5.6],
#     [5.8, 5.7, 5.6, 5.7],
#     [5.9, 5.8, 5.7, 5.8]]

# F = np.matrix(F)

F = [5.3, 5.4, 5.5, 5.4, 5.5, 5.4, 5.5, 5.6, 5.6, 5.6, 5.6, 5.6, 5.8, 5.7, 5.6, 5.7, 5.9, 5.8, 5.7, 5.8]
F = np.array(F)

# V = [[5.3, 5.3, 5.3, 5.4],
#      [5.4, 5.3, 5.4, 5.5],
#      [5.5, 5.4, 5.5, 5.5], 
#      [5.7, 5.5, 5.6, 5.6],
#      [5.8, 5.7, 5.6, 5.6]]

V = [5.3, 5.3, 5.3, 5.4, 5.4, 5.3, 5.4, 5.5, 5.5, 5.4, 5.5, 5.5, 5.7, 5.5, 5.6, 5.6, 5.8, 5.7, 5.6, 5.6]
V = np.array(V)
# V = np.matrix(V)

# %%
# a) Mean forecast error
# sum_F = 0
# count = 0
# for elem in F:
#     sum_F = sum_F + elem
#     count = count + 1
# F_ave = sum_F/count

F_ave = (F.sum(axis =0, dtype='float'))/len(F)
V_ave = (V.sum(axis =0, dtype='float'))/len(F)

ME = F_ave - V_ave
print('The mean forecast error is', ME)

# %%
# b) mean persistence error

# c) mean absolute forecast error

# d) mean squared forecast error

# e) mean squared climatology error

# f) mean squared forecast error skill score

# g) RMS forecast score

# h) correlation coefficient between forecast and verification

# i) forecast anomoly correlation

# j) persistence anomaly correlation

# k) draw height contours by hand 
