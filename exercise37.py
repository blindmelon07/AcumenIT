import csv
persons = [ {
    "name": "John",
    "movie": ["The Shawshank Redemption", "The Godfather"],
    "motto": "Don't let the noise of others' opinions drown out your own inner voice.",
    "age": 10,
}

]


with open ("persons.csv", "w", newline="") as csvfile:
    fieldnames = ["name", "movie", "motto", "age"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for person in persons:
        person["movie"] = ",".join(person["movie"])
        writer.writerow(person)
