import glob as glob
import pandas as pd
import numpy as np
import os

"""
This function will merged individual race result csv
and clean up the data using pandas

merge_csv function will merge the .csv

cleaner

output will have a sanitized and cleaned csv that will fit right into
the SQLite database as insert columns
"""

in_path = '../../output_scraped/'
out_path = '../../sanitized_data/'
print("Type the output file name that contains data to export")
print("make sure to add '.csv' file extension")
out_csv = input('> ')


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

    # adding DNS/DNF/DQ flags
    df_rename['Flag_DNS'] = np.where(df_rename['Time_Finish'] == 'DNS', 1, 0)
    df_rename['Flag_DNF'] = np.where(df_rename['Time_Finish'] == 'DNF', 1, 0)
    df_rename['Flag_DQ'] = np.where(df_rename['Time_Finish'] == 'DQ', 1, 0)

    # turn '---' into appropriate zeroes
    df_clean1 = df_rename.replace({
        'Rank_AG': '---',
        'Rank_Gender': '---',
        'Rank_Overall': '---',
        'Points': '---',
    }, 0)

    df_clean2 = df_clean1.replace({
        'Time_Swim': '---',
        'Time_Bike': '---',
        'Time_Run': '---',
        'Time_Finish': '---',
    }, '00:00:00')

    df_clean3 = df_clean2.replace({'Time_Finish':'DNS'},'00:00:00')
    df_clean4 = df_clean3.replace({'Time_Finish':'DNF'},'00:00:00')
    df_end = df_clean4.replace({'Time_Finish':'DQ'},'00:00:00')

    names = df_end['Athelete_Name'].str.split(', ', expand=True)
    df_end['Last_Name'] = names[0]
    df_end['First_Name'] = names[1]

    # save the cleaned DataFrame to csv at the defined path
    df_end.to_csv(out_path+out_csv, index=False, header=True)


if __name__ == "__main__":

    df = merge_csv(in_path)
    cleaner(df, out_path, out_csv)
