import pandas as pd
import numpy as np

path = '/home/amuweee/Dropbox/webscrape/im1406/ALL/'

url_prefix = 'http://www.ironman.com/triathlon/events/'


url_region = 'americas'
url_distance = 'ironman'
url_location = 'maryland'
url_race = 'maryland'

dates = {
    '2018' : '20180929',
    '2017' : '20171014',
    '2016' : '20161008',
    '2015' : '20151010',
    '2014' : '20141011',
    '2013' : '20131012',
    '2012' : '20121013',
    '2011' : '20111008',
}

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
    '90+Plus'
]

'http://www.ironman.com/triathlon/events/americas/ironman/maryland/results.aspx?race=maryland&rd=20180929&y=2018&sex=F&agegroup=30-34&loc='

df = pd.DataFrame()
df_csv = pd.DataFrame()
list = []

for url_y, url_rd in (dates.items()):
    for url_sex in sex:
        for url_cat in age_group:
            url_page = 1
            while True:
                try:
                    url = f'{url_prefix}/{url_region}/{url_distance}/{url_location}/results.aspx?p={url_page}&race={url_race}&rd={url_rd}&agegroup={url_cat}&sex={url_sex}&y={url_y}&ps=20'
                    website = pd.read_html(url, index_col=None, header=0)
                    df = pd.concat(website)
                    df['Gender'] = url_sex
                    df['Race_Year'] = url_y
                    df['Race_Date'] = url_rd
                    df['Race_Name'] = url_race
                    df['Age_Group'] = url_cat
                    list.append(df)
                    print(website)
                    url_page += 1
                except ValueError:
                    print(f'######### End of {url_race}-{url_y}-{url_sex}-{url_cat} #########')
                    break
df_csv = pd.concat(list)
df_csv.to_csv(path+f"{url_race}.csv", index=False, header=True)
