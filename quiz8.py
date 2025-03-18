#enhance the quiz7 so that you can save the result in csv
#either csv or txt
#quiz8 will not show the orders
import csv
import functions.pos
functions.pos.show_menu()
orders = functions.pos.get_orders()
with open('orders.csv', 'w', newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["fruits", "quantity", "total"])
    for order in orders:
        writer.writerow(order)

 

