import glob
import pandas as pd
import os

path = f'/home/amuweee/Dropbox/Python/git_ironman/ironman_tri/output_scraped/'
out_csv = 'ironman_2018.csv'
all_files = glob.glob(path + "*.csv")
df = pd.DataFrame()
l = []
for file in all_files:
    df = pd.read_csv(file, index_col=None, header=0)
    l.append(df)
merged = pd.concat(l)

merged.to_csv(path+out_csv)
