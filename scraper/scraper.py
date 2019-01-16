
import pandas as pd
import numpy as np

path = '/home/amuweee/Dropbox/Python/git_ironman/ironman_tri/output_scraped/'
file = 'ironman_20181231'

"""
arg for the race case must be a list in this order:

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
            '18-24','25-29',
            '30-34','35-39',
            '40-44','45-49',
            '50-54','55-59',
            '60-64','65-69',
            '70-74','75-79',
            '80-84','85-89',
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
                        df['Gender'] = url_sex
                        df['Race_Year'] = self.url_year
                        df['Race_Date'] = self.url_date
                        df['Race_Name'] = self.url_race
                        df['Age_Group'] = url_cat
                        results.append(df)
                        print(website)
                        url_page += 1
                    except ValueError:
                        print(f'######### End of #########')
                        break

        df_csv = pd.concat(results)
        df_csv.to_csv(path+f"{file}.csv", index=False, header=True)
