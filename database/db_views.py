import sqlite3


conn = sqlite3.connect('../../ironman.db')
c = conn.cursor()


def view_atheletes():

    # first, drops the view and rebuild from ironman_races table
    c.execute("DROP VIEW IF EXISTS atheletes")
    conn.commit()

    # create the view
    c.execute("""
        CREATE VIEW IF NOT EXISTS atheletes AS
            SELECT
                Athelete_Name,
                Last_Name,
                First_Name,
                Athelete_Country,
                Gender,
                COUNT(Athelete_Name) AS Race_Entered,
                SUM(Flag_DNS) AS DNS_Count,
                SUM(Flag_DNF) AS DNF_Count,
                SUM(Flag_DQ) AS DQ_Count
            FROM ironman_race
            GROUP BY 1,2,3,4,5
            ORDER BY race_entered desc
    """)
    conn.commit()


if __name__ == '__main__':

    view_atheletes()
    c.close()
    conn.close()
