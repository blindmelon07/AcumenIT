def add(*args):
    total = 0
    for value in args:
        total += value
        #total = total + value
    return total

print(add(1,2,3,4,5,6,7,8,9,10))



person = {
    "name": "John",
    "age": 36,
    "country": "Norway"
}
def showinfo(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")

print(showinfo(**person))


def print_all(*args, **kwargs):
   output = ""
   for arg in args:
       output += str(arg) + "\n"
   for key, value in kwargs.items():
       output += f"{key} = {value} "
   print(output)

print_all(1,2,3,4,5,6,7,8,9,10, name="John", age=36, country="Norway")
