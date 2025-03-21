from pathlib import Path
p = Path(".")
for file in p.iterdir():
    if file.is_dir():
        print(f"{file} (dir)")
    elif file.is_file():

        print(file)

p2 = p / Path("..")
for file in p2.iterdir():
    # print(file.absolute())
      print(file.resolve())



print("=======")

for file in p.itemdir():
    print(f"{file}: {stat.st_mtime}")