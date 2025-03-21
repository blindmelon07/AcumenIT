from pathlib import Path
file = Path("jokes.db")

with file.open("rb") as f:
    print(f.read())

data = file.read_text()
print(data)