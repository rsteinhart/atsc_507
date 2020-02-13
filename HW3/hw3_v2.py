# %% [markdown]
# ATSC 507 - HW3  
# Rachel Steinhart  
# February 12th, 2020  

# %%
import pandas as pd
import matplotlib.pyplot as plt
import math
import numpy as np

# %%
# Take out all the rows with "segment", "rant" and "points"
# to only leave lat & long coords. and make new files

files = ['africa-cil.txt', 'asia-cil.txt', 'europe-cil.txt', 
         'namer-cil.txt', 'samer-cil.txt']
bad_words = ['segment', 'rank', 'points']
new = 'new-'
for elem in files:
    with open(elem) as oldfile, open(new+elem, 'w') as newfile:
        for line in oldfile:
            if not any(bad_word in line for bad_word in bad_words):
                newfile.write(line)
# %%
#Take new files and form cumulative pandas dataframe
df_total = pd.DataFrame({'lat': [ ], 'long': [ ]}) #initialize dataframe
new_files = ['new-africa-cil.txt','new-asia-cil.txt', 'new-europe-cil.txt', 
             'new-namer-cil.txt', 'new-samer-cil.txt']

for elem in new_files:
    df = pd.read_csv(elem, sep=' ')
    df.columns = ['lat', 'long']
    df_total = df_total.append(df) 
    #add the coordinates from each file to the total file
# %%
df_total = df_total[df_total['long']>=-180] #remove any incorrect data
df_total = df_total[df_total['lat']>=0] #Specify Nothern Hemisphere only

# %%
fig, ax = plt.subplots(figsize=(20, 6))
ax.plot(df_total['long'],df_total['lat'],'.', markersize=0.02)
ax.set_xlabel('longitude (degrees)')
ax.set_ylabel('latitude (degreed)')
ax.set_title('Lat/Long grid of the Nothern Hemisphere');
#plt.savefig('Q1_pt1.png')

# %%
# Transform data into polar steriographic form
# Using equation from Stull pg.748

phi0 = 60 # projection plane at latitude of 60 degrees
phi = df_total['lat']
R0 = 6371 #km
rad = np.pi/180

L = R0*(1+np.sin(phi0*rad))
r = L*np.tan(0.5*(90-phi)*rad)

x = r*np.cos(df_total['long']*rad)
y = r*np.sin(df_total['long']*rad)

# %%
#Plot polar steriographic coordinates
fig, ax = plt.subplots(figsize=(10,10))
ax.plot(x,y,'.', markersize=0.02)
ax.set_xlabel('x (km)')
ax.set_ylabel('y (km)')
ax.set_title('Polar steriographic projection of the Nothern Hemisphere');

# %%
