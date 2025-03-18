import csv

##reading csv file
with open('voting.csv', 'r', newline="") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)




print("=" * 20)



with open('voting.csv', 'r', newline="") as f:
    reader = csv.reader(f)
    data = list(reader)
    for row in reader:
        print(row)