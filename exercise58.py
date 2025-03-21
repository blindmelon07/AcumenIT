from pathlib import Path


file1 = Path("hello.txt")
file2 = file1.with_suffix(".csv")
file2 = file2.with_name("hello2.txt")


print(file1)
print(file2)    
# file1.rename(file2)
file1.replace(file2)