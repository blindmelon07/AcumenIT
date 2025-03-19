def greet(time="12:00"):
    print("Hello!")
    print(f"It's {time}")

greet()



def add(a, b):
    return a + b
if __name__ == "__main__":
    ret = greet()
    print(ret)
    ret = add(1, 1)
    print(ret)
