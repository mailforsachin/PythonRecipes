
import sqlite3
import config

conn=sqlite3.connect(config.DATABASE_LOCATION)
cursor=conn.cursor();
cursor.execute('''drop table users''')
cursor.execute('''
       CREATE TABLE IF NOT EXISTS d_users (
           id INTEGER PRIMARY KEY,
           name TEXT NOT NULL,
           age INTEGER,
           email TEXT
       )
   ''')
conn.commit()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables=cursor.fetchall();
for table in tables:
    print(table[0])