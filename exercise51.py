import sqlite3
conn = sqlite3.connect(":memory:")
curr = conn.cursor()

# curr.execute("""
#     CREATE TABLE IF NOT EXISTS users (
#         id INTEGER PRIMARY KEY,
#         username TEXT NOT NULL,
#         password TEXT NOT NULL
#     )
# """)


curr.execute("CREATE TABLE movie (title, year, score)")


data = [
    ("Monty Python and the Holy Grail", 1975, 8.2),
    ("And Now for Something Completely Different", 1971, 7.5),
]
curr.executemany("INSERT INTO movie VALUES(?, ?, ?)", data)
conn.commit()

# res = curr.execute("SELECT * FROM movie")
# print(res.fetchall())

for row in curr.execute("SELECT * FROM movie"):
    print(row)


conn.close()