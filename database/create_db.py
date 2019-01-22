"""
Creates a localhosted SQLite3 DB
"""

import sqlite3

conn = sqlite3.connect(':memory:')

c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS ironman(

            )""")

conn.commit()

conn.close()
