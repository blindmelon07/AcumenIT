#make a calculator use a function

def add(x,y):
    return x + y  # Pagdadagdag (addition)
def subtract(x,y):
    return x - y  # Pagbabawas (subtraction)
def multiply(x,y):
    return x * y  # Pagpaparami (multiplication)
def divide(x,y):
    return x / y  # Paghahati (division)

# Kuha ng mga numero mula sa user
def get_inputs():
    return int(input("Enter first number: ")), int(input("Enter second number: "))  # Kumuha ng dalawang integer input

# Kuha ng operator mula sa user
def get_operator():
    return input("Enter operator (+, -, *, /): ")  # Tanggapin ang operator

# Ipakita ang resulta
def print_result(result):
        print("Result: ", result)  # Mag-print ng resulta

# Pangunahing logic ng calculator
def main():
    operations = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide
    }  # Dictionary ng mga operasyon
    
    while True:  # Walang hanggang loop hanggang mag-exit ang user
        try:
            num1, num2 = get_inputs()  # Kunin ang mga numero
            op = get_operator()  # Kunin ang operator
            
            if op not in operations:
                print("Invalid operator! Please use +, -, *, /")  # Error sa invalid operator
                continue  # Balik sa simula ng loop
                
            result = operations[op](num1, num2)  # Tawagin ang tamang operasyon
            print_result(result)  # Ipakita ang resulta
            
            if input("Another calculation? (y/n): ").lower() != 'y':
                print("Goodbye!")  # Paalam message
                break  # Tapusin ang loop
                
        except ZeroDivisionError:
            print("Error: Cannot divide by zero!")  # Error sa paghahati sa zero
        except ValueError:
            print("Error: Please enter valid numbers!")  # Error sa invalid numbers

# Simula ng programa
if __name__ == '__main__':
    print("Calculator")  # Title ng calculator
    main()  # Tumawag sa pangunahing function