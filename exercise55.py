import sqlite3
filename = "data.db"
conn = sqlite3.connect("data.db")
curr = conn.cursor()


sql = """SELECT year, title  FROM movie ORDER BY year = 1975 """





curr.execute(sql)
print(curr.fetchall())

conn.close()
