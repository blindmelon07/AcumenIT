from pathlib import Path

for root, dirs, files in Path(".").walk():
    print(root, dirs, files)

    print("=======")

    for root, dirs, files in Path(".").walk():
        for file in files:
            print(root / file)