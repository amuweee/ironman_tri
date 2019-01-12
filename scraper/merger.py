import glob
import pandas as pd
import os

date = '20181014'
path = f'/home/amuweee/Dropbox/webscrape/im1406/ALL/'
allFiles = glob.glob(path + "*.csv")
frame = pd.DataFrame()
list_ = []
for file_ in allFiles:
    df = pd.read_csv(file_, index_col=None, header=0)
    list_.append(df)
frame = pd.concat(list_)

frame.to_csv(f'{path}clean/{date}.csv')
