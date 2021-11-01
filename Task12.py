"""Write a program that counts how many times each of the numbers has appeared in the prepared table and prints a summary in the console. An array can contain ** only ** numbers from 1 to 10.

For example, for the table `[6 5 4 5 10 5 8 3 10 6 6 6 4 3 2 8 1 3 4 7] ', the program should write in the console the number of occurrences of each number:

1 - 1
2 - 1
3 - 3
4 - 3
5 - 3
6 - 4
7 - 1
8 - 2
9 - 0
10 - 2
An array containing numbers is prepared as the variable numbers.

def program(numbers):
    # Implement your solution here

# Do not change code below this line
data = list()
amount = int(input())
for i in range(amount):
    data.append(int(input()))

program(data)
"""
try:
    numbers = ("6", "5", "4", "5", "10", "5", "8", "3")
    unique = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0}

    for value in numbers:
        if value in unique.keys():
            unique[value] += 1
    for x, y in unique.items():
        print(x, "-", y)
except:
    print("Please enter valid numbers!")



