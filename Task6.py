"""Write a program that takes from the user two integers A - a (int) and B - b (int), where A < B, and then calculates the sum of the sequence of numbers from A to B (A, A + 1, A + 2, ..., B) and prints it in the console. When the A < B condition is not met, the program exits by writing Job finished in the console.

For example, for A = 4 and B = 11, the program should write the number 60 in the console.

Get data from the user in the console using argument-less input()."""

import abc

try:
    a = int(input(""))
    b = int(input(""))
    c = a
    if a >= b:
        print("Job finished")
    elif a < b:
        while a < b:
            a = a+1
            c= c+a
        print(c)
except:
    print("Please enter only numbers.")