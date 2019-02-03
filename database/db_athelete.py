"""
initialize a row of cleaned athelete detail as a list
and turn into variable that will be used for sql insert
"""


class athelete:

    def __init__(self, bib):
        self.athelete_name = bib[0]
        self.athelte_country = bib[1]
        self.rank_ag = bib[2]
        self.rank_gender = bib[3]
        self.rank_overall = bib[4]
        self.time_swim = bib[5]
        self.time_bike = bib[6]
        self.time_run = bib[7]
        self.time_finish = bib[8]
        self.points = bib[9]
        self.distance = bib[10]
        self.race_city = bib[11]
        self.race_country = bib[12]
        self.race_region = bib[13]
        self.gender = bib[14]
        self.race_year = bib[15]
        self.race_date = bib[16]
        self.race_name = bib[17]
        self.age_group = bib[18]
        self.flag_dns = bib[19]
        self.flag_dnf = bib[20]
        self.flag_dq = bib[21]
        self.last_name = bib[22]
        self.first_name = bib[23]
