import pprint 

person = {
    "name": "John",
    "movie": ["The Shawshank Redemption", "The Godfather"],
    "motto": "Don't let the noise of others' opinions drown out your own inner voice.",
    "age": 10,
}
#to print keys in the dictionary
for key in person:
    print(key)

    print("===" * 20)

##to print values in the dictionary
    for value in person.values():
        print(value)

#to print both keys and values in the dictionary
    for key, value in person.items():
        print(f"{key} = {value}")
        