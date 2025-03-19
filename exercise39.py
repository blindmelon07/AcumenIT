from _typeshed import DataclassInstance
import json
from os import write

persons = [ 
    {
    "name": "John",
    "movie": ["The Shawshank Redemption", "The Godfather"],
    "motto": "Don't let the noise of others' opinions drown out your own inner voice.",
    "age": 10,
}
]


with open("persons.json", "w") as f:
    data = json.dumps(persons)
    f.write(data)
    