from pathlib import Path

file = Path("jokes.db")    
print(file.exists())


print(type(file))
print(str(file))


file2 = Path("hello.txt.json")
print(file2.suffix)
print(file2.suffixes)