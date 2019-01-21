"""
Creates a localhosted SQLite3 DB
"""

import sqlite3

conn = sqlite3.connect('im_races.db')

c = conn.cursor()

c.execute("""CREATE TABLE ironman(

            )""")

conn.commit()

conn.close()
