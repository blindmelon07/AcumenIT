#based on quize6 create functions for the following
#show menu
#ask for orders
#print orders
#you may add more functions if needed 

fruits = {
    "Apple": 2.50,
    "Banana": 1.50,
    "Orange": 2.00,
    "Mango": 3.50,
    "Grape": 4.00,
}
def show_menu():
    print("Welcome to the Fruit Store!")
    print("\nFruits Menu:")
    print("-" * 20)
    for fruit, price in fruits.items():
        print(f"{fruit}: ${price:.2f}")
    print("-" * 20)

def get_orders():
    orders = []
    while True:
        fruit = input("Enter the fruit name (or 'cancel' to Cancel transaction): ").title().strip()
        if fruit.lower() == 'cancel':
            break
        if fruit in fruits:
            quantity = int(input("Enter the quantity: "))
            orders.append((fruit, quantity))
        else:
            print("Invalid fruit name. Please try again.")
    return orders

def print_orders(orders):
    print("\nYour Orders:")
    print("-" * 20)
    for fruit, quantity in orders:
        price = fruits[fruit]
        total_price = price * quantity
        print(f"{fruit}: {quantity} x ${price:.2f} = ${total_price:.2f}")
    print("-" * 20)

if __name__ == "__main__":
    show_menu()
    orders = get_orders()
    print_orders(orders)