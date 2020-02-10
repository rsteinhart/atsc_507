# %%
import pandas as pd


# %% 
# Take out all the rows with segment, rant and points 
# to only leave latlong coords.
files = ['africa-cil.txt', 'asia-cil.txt', 'europe-cil.txt', 'namer-cil.txt', 'samer-cil.txt']
bad_words = ['segment', 'rank', 'points']
new = 'new-'
for elem in files:
    with open(elem) as oldfile, open(new+elem, 'w') as newfile:
        for line in oldfile:
            if not any(bad_word in line for bad_word in bad_words):
                newfile.write(line)
# c = pd.read_csv('africa-cil-new.txt')
# print(c)
# %%
new_files = ['new-africa-cil.txt', 'new-asia-cil.txt', 'new-europe-cil.txt', 'new-namer-cil.txt', 'new-samer-cil.txt']
for elem in new_files:
    df = pd.read_csv(elem)
    df.columns = ['lat', 'long']

# %%
