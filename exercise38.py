import csv

with open("persons.csv", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        row["age"] = int(row["age"])
        row["movie"] = row["movie"].split(",")
        print(row)