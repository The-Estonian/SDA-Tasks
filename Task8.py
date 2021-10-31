"""Write a program that takes numbers from the user as long as the number 0 is not given. When the number 0 is given, the program calculates the sum of the numbers given and prints it in the console.

For example, for a series of given numbers: 3, 2, 5, 1, 0, the program should write the number 11 in the console.   Get data from the user in the console using argument-less input()."""
try:
    count = 0
    while True:
        number = int(input())
        if number > 0 or number < 0:
            count += number
        if number == 0:
            break
    print(count)
except:
    print("Please enter valid numbers")