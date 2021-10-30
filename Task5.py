"""Write a program that takes a positive integer from the user - number (int), and then prints all positive odd numbers not greater than the given number in the console in order.

For example, for the number 15, the program should write in the console the numbers: 1, 3, 5, 7, 9, 11, 13, 15.

Get data from the user in the console using argument-less input()."""

# Code
try:
    number = int(input())
    for i in range(0, number+1):
        if i % 2 != 0:
            print(i)
except:
    print("Please enter a positive number")