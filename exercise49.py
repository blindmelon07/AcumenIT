# data type function
def greet_morning():
    print("Good morning")
def greet_afternoon():
    print("Good afternoon")
def greet_evening():
    print("Good evening")

greetings = {
    1: greet_morning,
    2: greet_afternoon,
    3: greet_evening,
}

choice = int(input("Enter a number: "))
func = greetings.get(choice)
if func is None:
    print("Invalid choice")
else:
    func()