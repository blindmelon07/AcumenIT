#make a program that appends the even numbers 
#from a list of new list.
#Print the new list. use for loops
#This code creates a list of numbers from 1 to 10.
#It then creates an empty list called even_numbers.
#It then loops through the numbers list and checks if the number is even by using the modulo operator %.
#If the number is even, it appends it to the even_numbers list.
#Finally, it prints the even_numbers list.
#The output of this code will be [2, 4, 6, 8, 10].
#Example:
numbers = [1,2,3,4,5,6,7,8,9,10]
even_numbers = []
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
print(even_numbers)


