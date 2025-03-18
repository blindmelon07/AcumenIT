#while loops
#loops: break(leave the loop. can be used in the for and while loops), continue, pass
while True:
    print("hello world")
    choice  = input("do you want to continue [Y/N]?").lower()

    if choice == "n":
        break
    elif choice != "y":
     print("not a valid choice . try again")
    continue
