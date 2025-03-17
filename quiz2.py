
numbers = [1,2,3,4,5,6,7,8,9,10]
even_numbers = []
odds = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odds.append(number)
print(even_numbers)
print(odds)

