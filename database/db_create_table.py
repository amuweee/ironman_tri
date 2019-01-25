import sqlite3


conn = sqlite3.connect('ironman.db')
c = conn.cursor()

def create_table():

    c.execute("""
        CREATE TABLE IF NOT EXISTS ironman_race(
            Athelete_Name TEXT,
            Athelete_Country TEXT,
            Rank_AG INTEGER,
            Rank_Gender INTEGER,
            Rank_Overall INTEGER,
            Time_Swim TEXT,
            Time_Bike TEXT,
            Time_Run TEXT,
            Time_Finish TEXT,
            Points INTEGER,
            Distance TEXT,
            Race_City TEXT,
            Race_Country TEXT,
            Race_Region TEXT,
            Gender TEXT,
            Race_Year INTEGER,
            Race_Date TEXT,
            Race_Name TEXT,
            Age_Group TEXT,
            Flag_DNS INTEGER,
            Flag_DNF INTEGER,
            Flag_DQ INTEGER,
            Meta INTEGER,
            UNIQUE (Athelete_Name,
                    Distance,
                    Rank_Overall,
                    Race_Date,
                    Time_Swim,
                    Time_Bike,
                    Time_Run,
                    Time_Finish,
                    Race_Name)
        )""")

    conn.commit()


if __name__ == '__main__':

    create_table()
    c.close()
    conn.close()
