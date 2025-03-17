fruits = ["apple", "banana", "strawberry", "banana"]
# print(fruits.index("banana"))

# del fruits[1]
# print(fruits)



i = fruits.index("banana")
print(i) #1
i = fruits.index("banana", i+1)
print(i)
del fruits[i]
print(fruits)
