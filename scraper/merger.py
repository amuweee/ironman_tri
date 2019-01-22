import glob as glob
import pandas as pd
import os

"""
This function will merged individual race result csv
and clean up the data using pandas

merge_csv function will merge the .csv

cleaner

output will have a sanitized and cleaned csv that will fit right into
the SQLite database as insert columns
"""

in_path = '/home/amuweee/Dropbox/Python/git_ironman/ironman_tri/database/output_scraped/'
out_path = '/home/amuweee/Dropbox/Python/git_ironman/ironman_tri/database/sanitized_data/'
out_csv = 'ironman_2018.csv'


def merge_csv(in_path):

    input_files = glob.glob(in_path + '*.csv')
    df = pd.DataFrame()
    l = []
    for file in input_files:
        df = pd.read_csv(file, index_col=None, header=0)
        l.append(df)
    merged = pd.concat(l)

    return merged


def cleaner(df, out_path, out_csv):

    # rename column names
    df_rename = df.rename(index=str, columns={
        'Name': 'Athelete_Name',
        'Country': 'Athelete_Country',
        'Div Rank': 'Rank_AG',
        'Gender Rank': 'Rank_Gender',
        'Overall Rank': 'Rank_Overall',
        'Swim': 'Time_Swim',
        'Bike': 'Time_Bike',
        'Run': 'Time_Run',
        'Finish': 'Time_Finish',
    })


    # save the cleaned DataFrame to csv at the defined path
    df_end.to_csv(out_path+f"{out_csv}.csv", index=False, header=True)



if __name__ == "__main__":

    df = merge_csv(in_path)
    cleaner(df, out_path, out_csv)
