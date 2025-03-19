def greet(time="morning"):
    # print(f"Good {time}, use")
    try:
        1 / 0
    except ZeroDivisionError:
        print("You cannot divide by zero you idiot")
    raise

try:
    greet()
except ZeroDivisionError:
    print("Good morning, use")
except:
    print("Good morning, use")
