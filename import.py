import sqlite3
import pandas as pd

df = pd.read_csv('meibo.csv')
dbname = 'db.sqlite3'

con = sqlite3.connect(dbname)
cur = con.cursor()

df.to_sql('myapp_meibo', con, if_exists = 'append', index_label = 'id')

cur.close()
con.close()

