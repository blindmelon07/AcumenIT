import csv

with open('orders.csv', 'r') as f:
    reader = csv.reader(f)
    headers = next(reader)
    
    print("\nSales Records:")
    print("-" * 40)
    print(f"{headers[0]:<15} | {headers[1]:<8} | {headers[2]}")
    print("-" * 40)
    
    for row in reader:
        fruit, price, quantity = row
        print(f"{fruit:<15} | ${float(price):<7.2f} | {quantity} items")