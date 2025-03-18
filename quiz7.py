# from pos import *
# import python.functions.pos
from functions import pos
from functions import auth

auth.login()
pos.show_menu()

orders = pos.get_orders()

pos.print_orders(orders)
