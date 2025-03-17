#make a program that converts a list of fruits into upper cases
#put the new upper case fruits into a new list
#use for loops to iterate through the list



fruits = [
    "apple", 
    "banana", 
    "strawberry",
    "kiwi", 
    "orange"
    ]
fruits_upper = []

for fruit in fruits:
    fruits_upper.append(fruit.upper())

print(fruits_upper)


fruits.sort(reverse=False)
print(fruits_upper)

