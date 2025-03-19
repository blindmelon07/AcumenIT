#data type:DICT
person = {
    "name": "John",
    "movie": ["The Shawshank Redemption", "The Godfather"],
    "motto": "Don't let the noise of others' opinions drown out your own inner voice."
}
print (person)
print (person["name"])
print (person["movie"])
print (person["motto"])

person ["accolades"] = "Best Picture"
print (person["accolades"])
print('age' in person)
print("age" not in person)
print(person.get("age"))
print(person.get("age", "not found"))
print(person.get("movie", "not found"))
#.remove
person["movie"].remove("The Godfather")
##delete a key value 
del person["movie"] 
print(person)