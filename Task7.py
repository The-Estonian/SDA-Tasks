"""Write a program that takes a positive integer N - n (int) from the user, and then displays all powers of the number 2 in the console that are not greater than the number given.

For example, for the number 71 the program should write in the console the numbers: 1 2 4 8 16 32 64.

Get data from the user in the console using argument-less input()."""
try:
    n = int(input())
    i = 1
    while i <= n:
        print(i)
        i *= 2
except:
    print("Please enter numerical value.")












