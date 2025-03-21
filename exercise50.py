#data type: multiline string


data = """
hello world
 """
print(data)
print(data.count("\n"))

data = "\n\nhello world\n\n"
print(data)
print(data.count("\n"))