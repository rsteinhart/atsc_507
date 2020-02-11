# %%
import pandas as pd
#import pylab as pl
import matplotlib.pyplot as plt

# %% 
# Take out all the rows with segment, rant and points 
# to only leave latlong coords. and make new files
#files = ['africa-cil.txt', 'asia-cil.txt', 'europe-cil.txt', 'namer-cil.txt', 'samer-cil.txt']
files = ['asia-cil.txt', 'europe-cil.txt', 'namer-cil.txt']
bad_words = ['segment', 'rank', 'points']
new = 'new-'
for elem in files:
    with open(elem) as oldfile, open(new+elem, 'w') as newfile:
        for line in oldfile:
            if not any(bad_word in line for bad_word in bad_words):
                newfile.write(line)
# c = pd.read_csv('new-africa-cil.txt')
# print(c)
# %%
df_total = pd.DataFrame({'lat': [ ], 'long': [ ]})
#new_files = ['new-africa-cil.txt','new-asia-cil.txt', 'new-europe-cil.txt', 'new-namer-cil.txt', 'new-samer-cil.txt']
new_files = ['new-asia-cil.txt', 'new-europe-cil.txt', 'new-namer-cil.txt']

for elem in new_files:
    df = pd.read_csv(elem, sep=' ')
    df.columns = ['lat', 'long']
    df_total = df_total.append(df)
    #print(df_total)
    #df_total.columns = ['lat', 'long']
# %%
#Delete unnecessary data
#df_total[df_total > -400].dropna()
# Get names of indexes for which column Age has value 30
indexNames = df_total[df_total['long'] < -400].index
print(indexNames)
# Delete these row indexes from dataFrame
df_total.drop(index=indexNames)
# %%
#df_total.plot(x = 'long', y='lat', kind='scatter')
#df_total.plot(x = 'long', y='lat')
plt.plot(df_total['long'],df_total['lat'],'.', markersize=0.2)
plt.show()
#plt.savefig('Q1_pt1.png')
# %%
#Space between old and new code
#
#
#
# %%
# df_africa = pd.read_csv('new-africa-cil.txt', sep=' ')
# #print(df_africa)
# df_africa.columns = ['lat', 'long']

# df_asia = pd.read_csv('new-asia-cil.txt', sep=' ')
# df_asia.columns = ['lat', 'long']

# df_europe = pd.read_csv('new-europe-cil.txt', sep=' ')
# df_europe.columns = ['lat', 'long']

# df_namer = pd.read_csv('new-namer-cil.txt', sep=' ')
# df_namer.columns = ['lat', 'long']

# df_samer = pd.read_csv('new-samer-cil.txt', sep=' ')
# df_samer.columns = ['lat', 'long']

# df1 = df_africa.append(df_asia)
# df2 = df1.append(df_europe)
# #print(df2)
# df3 = df2.append(df_namer)
# df4 = df3.append(df_samer)
# #print(df4)
# # %%
# df4.plot(x = 'long', y='lat', kind='scatter')

# lat_coords = df4['lat']
# long_coords = df4['long']
# plt.scatter(long_coords,lat_coords)



# %%
