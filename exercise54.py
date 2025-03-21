import sqlite3
conn = sqlite3.connect("data.db")
curr = conn.cursor()

data = [
    ("Montasdasdasd", 1975, 8.2),
    ("And Now for Something Completely Different", 1971, 7.5),
]
with conn:
    curr.executemany("INSERT INTO movie (title, year, score)VALUES(?, ?, ?)", data)
# conn.commit()

conn.close()
