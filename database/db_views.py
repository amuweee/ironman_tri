import sqlite3


conn = sqlite3.connect('../../ironman.db')
c = conn.cursor()


def create_views():

    # first, drops the view and rebuild from ironman_races table
    c.execute("DROP VIEW IF EXISTS atheletes_v")
    c.execute("DROP VIEW IF EXISTS races_v")
    conn.commit()

    # create atheletes view
    c.execute("""
        CREATE VIEW IF NOT EXISTS atheletes_v AS
            SELECT
                athelete_name,
                last_name,
                first_name,
                athelete_country,
                gender,
                SUM(CASE WHEN distance='Ironman 140.6' THEN 1 ELSE 0 END) AS race_entered_full,
                SUM(CASE WHEN distance='Ironman 70.3' THEN 1 ELSE 0 END) AS race_entered_half,
                COUNT(athelete_name) AS race_entered_total,
                SUM(flag_dns) AS dns_count,
                SUM(flag_dnf) AS dnf_count,
                SUM(flag_dq) AS dq_count
            FROM ironman_race
            GROUP BY 1, 2, 3, 4, 5
            ORDER BY race_entered_total DESC
        """)
    conn.commit()


    # create races view
    c.execute("""
        CREATE VIEW IF NOT EXISTS races_v AS
            SELECT
                distance,
                race_name,
                race_region,
                race_country,
                COUNT(race_name) AS participants_total,
                SUM(CASE WHEN race_year = 2011 THEN 1 ELSE 0 END) AS participants_2011,
                SUM(CASE WHEN race_year = 2012 THEN 1 ELSE 0 END) AS participants_2012,
                SUM(CASE WHEN race_year = 2013 THEN 1 ELSE 0 END) AS participants_2013,
                SUM(CASE WHEN race_year = 2014 THEN 1 ELSE 0 END) AS participants_2014,
                SUM(CASE WHEN race_year = 2015 THEN 1 ELSE 0 END) AS participants_2015,
                SUM(CASE WHEN race_year = 2016 THEN 1 ELSE 0 END) AS participants_2016,
                SUM(CASE WHEN race_year = 2017 THEN 1 ELSE 0 END) AS participants_2017,
                SUM(CASE WHEN race_year = 2018 THEN 1 ELSE 0 END) AS participants_2018
            FROM ironman_race
            GROUP BY 1, 2, 3, 4
            ORDER BY participants_total DESC
        """)
    conn.commit()


if __name__ == '__main__':

    create_views()
    c.close()
    conn.close()
