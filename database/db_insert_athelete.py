import os
import time
import datetime
import sqlite3
import pandas as pd
from db_athelete import athelete

"""
arg for insert_athelete() must be a csv created from scraper/mergr.py
"""

path = '../../sanitized_data/'
print("Type the file that contains data to insert")
print("make sure to add '.csv' file extension")
file = input()
if os.path.isfile(path + file) == True:
    pass
else:
    print('files does not exist!')
    quit()


def insert_athelete(bib):

    ath = athelete(bib)

    # timestamp for insert metadata
    unix = time.time()
    dt = str(datetime.datetime.fromtimestamp(
        unix).strftime('%Y-%m-%d %H:%M:%S'))

    c.execute("""
        INSERT OR IGNORE INTO ironman_race
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
              (ath.athelete_name,
               ath.athelte_country,
               ath.rank_ag,
               ath.rank_gender,
               ath.rank_overall,
               ath.time_swim,
               ath.time_bike,
               ath.time_run,
               ath.time_finish,
               ath.points,
               ath.distance,
               ath.race_city,
               ath.race_country,
               ath.race_region,
               ath.gender,
               ath.race_year,
               ath.race_date,
               ath.race_name,
               ath.age_group,
               ath.flag_dns,
               ath.flag_dnf,
               ath.flag_dq,
               ath.last_name,
               ath.first_name,
               dt))


if __name__ == '__main__':

    conn = sqlite3.connect('../../ironman.db')
    c = conn.cursor()

    df = pd.read_csv(path + file, header=0)
    l = df.values.tolist()
    for row in l:
        insert_athelete(row)

    conn.commit()
    c.close()
    conn.close()
