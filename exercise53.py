import sqlite3
conn = sqlite3.connect("data.db")
curr = conn.cursor()

curr.execute("CREATE TABLE movie (title, year, score)")
conn.commit()
conn.close()
