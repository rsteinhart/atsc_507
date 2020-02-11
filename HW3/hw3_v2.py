# %%
import pandas as pd
import matplotlib.pyplot as plt
import math
import numpy as np

# %% 
# Take out all the rows with segment, rant and points 
# to only leave latlong coords. and make new files
files = ['africa-cil.txt', 'asia-cil.txt', 'europe-cil.txt', 'namer-cil.txt', 'samer-cil.txt']
bad_words = ['segment', 'rank', 'points']
new = 'new-'
for elem in files:
    with open(elem) as oldfile, open(new+elem, 'w') as newfile:
        for line in oldfile:
            if not any(bad_word in line for bad_word in bad_words):
                newfile.write(line)
# %%
#Take new files and form cumulative pandas dataframe
df_total = pd.DataFrame({'lat': [ ], 'long': [ ]})
new_files = ['new-africa-cil.txt','new-asia-cil.txt', 'new-europe-cil.txt', 'new-namer-cil.txt', 'new-samer-cil.txt']

for elem in new_files:
    df = pd.read_csv(elem, sep=' ')
    df.columns = ['lat', 'long']
    df_total = df_total.append(df)
# %%
#Specify Nothern Hemisphere only
df_total = df_total[df_total['long']>=-180]
df_total = df_total[df_total['lat']>=0]

# %%
plt.plot(df_total['long'],df_total['lat'],'.', markersize=0.1)
plt.show()
#plt.savefig('Q1_pt1.png')

# %% 
#Transform to polar sterio 
phi0 = 60
phi = df_total['lat']
R0 = 6371 #km
rad = np.pi/180

L = R0*(1+np.sin(phi0*rad))
r = L*np.tan(0.5*(90-phi)*rad)

x = r*np.cos(df_total['long']*rad)
y = r*np.sin(df_total['long']*rad)

# %%
#Plot polar steriographic coordinates
plt.plot(x,y,'.', markersize=0.1)
plt.show()