import glob
import pandas as pd
import os

"""
This function will merged individual race result csv
and clean up the data using pandas



"""

in_path = f'/home/amuweee/Dropbox/Python/git_ironman/ironman_tri/output_scraped/'
out_path = f'/home/amuweee/Dropbox/Python/git_ironman/ironman_tri/database/sanitized_data/'
out_csv = 'ironman_2018.csv'


def merge_csv(in_path, out_path, out_csv):

    input_files = glob.glob(in_path + '*.csv')
    df = pd.DataFrame()
    l = []
    for file in input_files:
        df = pd.read_csv(file, index_col=None, header=0)
        l.append(df)
    merged = pd.concat(l)

    return merged
