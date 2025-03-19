#exeption handling 
from os import name


class CustomError(Exception):
   pass


try:
    int("weeee")
    print(name)
    1 / 0
    raise CustomError("This is a custom error")
except ZeroDivisionError:
    print("You cannot divide by zero you idiot")
except (NameError, ValueError):
    print("You have not defined the variable")

except Exception as e:
    print("An error occurred:", e)
    print(str(e))
finally:
        print("This is the end of the program")