import pandas as pd
import numpy as np
import time

path = '../database/output_scraped/'
# path of output file

race_index = 'input.csv'

"""
arg for the race_index must be a list in this order:
race_index must be a list of lists

    1 - race_distance
    2 - race_city
    3 - race_country
    4 - region
    5 - url_region
    6 - url_distance
    7 - url_location
    8 - url_race
    9 - url_year
    10 - url_date

scraper() function will return a DataFrame of all the results
in the specific dace day
"""


class race:

    def __init__(self, para):

        self.race_distance = para[0]
        self.race_city = para[1]
        self.race_country = para[2]
        self.region = para[3]
        self.url_region = para[4]
        self.url_distance = para[5]
        self.url_location = para[6]
        self.url_race = para[7]
        self.url_year = para[8]
        self.url_date = para[9]

    def scraper(self):

        url_prefix = 'http://www.ironman.com/triathlon/events/'
        sex = ['M', 'F']
        age_group = [
            'Pro',
            '18-24', '25-29',
            '30-34', '35-39',
            '40-44', '45-49',
            '50-54', '55-59',
            '60-64', '65-69',
            '70-74', '75-79',
            '80-84', '85-89',
            '90+Plus']

        df = pd.DataFrame()
        df_csv = pd.DataFrame()
        results = []

        for url_sex in sex:
            for url_cat in age_group:
                url_page = 1
                while True:
                    try:
                        url = f'{url_prefix}/{self.url_region}/{self.url_distance}/{self.url_location}/results.aspx?p={url_page}&race={self.url_race}&rd={self.url_date}&agegroup={url_cat}&sex={url_sex}&y={self.url_year}&ps=20'
                        website = pd.read_html(url, index_col=None, header=0)
                        df = pd.concat(website)
                        df['Distance'] = self.race_distance
                        df['Race_City'] = self.race_city
                        df['Race_Country'] = self.race_country
                        df['Race_Region'] = self.region
                        df['Gender'] = url_sex
                        df['Race_Year'] = self.url_year
                        df['Race_Date'] = self.url_date
                        df['Race_Name'] = self.url_race
                        df['Age_Group'] = url_cat
                        results.append(df)
                        url_page += 1
                        time.sleep(0.5)
                    except ValueError:
                        print(f'######### Imported {url_page} pages from {self.url_location} || {self.url_date} || {url_sex} {url_cat} #########')
                        break

        df_csv = pd.concat(results)
        return df_csv


if __name__ == "__main__":

    df_input = pd.read_csv(race_index, header=0)
    ll = df_input.values.tolist()
    for instance in ll:
        r = race(instance)
        df_csv = r.scraper()
        name = f'{instance[5]}_{instance[7]}_{instance[9]}'
        df_csv.to_csv(path+f"{name}.csv", index=False, header=True)
