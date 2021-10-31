"""Write a program that takes an integer from the user and prints all its divisors in the console.

For example, for the number 21, the program should write in the console the numbers: 1, 3, 7, 21   Get data from the user in the console using argument-less input()."""
try:
    number = int(input("Please enter a number: "))
    for i in range(1, number+1):
        if number % i == 0:
            print(i)
except:
    print("Please enter a divisible number.")