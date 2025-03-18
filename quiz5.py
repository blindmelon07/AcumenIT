# Dictionary to store fruits and their prices
#  # Dictionaryo ng mga prutas at presyo
fruits = {
    "Apple": 2.50,
    "Banana": 1.50,
    "Orange": 2.00,
    "Mango": 3.50,
    "Grape": 4.00
}

# Show the menu # Pagpapakita ng menu
print("Welcome to the Fruit Store!")
print("\nFruits Menu:")
#create a visual separator 
print("-" * 20)

#for loop pinagsama na ung fruit at price sa fruits dictionary
#lalabas ang lahat ng records sa fruits list gamit ang loop
for fruit, price in fruits.items():
    print(f"{fruit}: ${price:.2f}")
##enndddddddd


#list o of the orders

#dito ma store ang mga napiling orders sa list gamit ang .Append method
orders = []
#eto din ang total ng orders sa list 
total = 0.0
# Ask the user for multiple orders using while loop pero dko pa sure
while True:
    choice = input("\nWhich fruit would you like to buy? ").title()
    if choice in fruits:
        quantity = int(input(f"How many {choice}s would you like to buy? "))
       #add to orders list  using append
        orders.append((choice, quantity))

        #add this to running total
        total += fruits[choice] * quantity
    else:
        print("Sorry, we don't have that fruit in stock.")
    another = input("Would you like to make another order? (yes/no) ").lower()
    if another != "yes":
        break
    #babalik sa pinaka taas o unang  bahagi ng while loop

# Print all the orders
print("\nYour orders:")
if orders:
    for fruits, quantity in orders:
        print(f"{quantity} {fruits}")
    print(f"Total: ${total:.2f}")
else:
    print("No orders were placed.")



