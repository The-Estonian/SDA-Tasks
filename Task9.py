"""Write a program that retrieves an integer string from the user. Downloading data ends with the number 0 (not included in the data). Then, the program calculates the sum of the largest and smallest of the given numbers and their arithmetic average and prints them in the console.

For example, for a series of given numbers: 1, -4, 2, 17, 0, the program should write in the console the numbers: 13, 6.5.   Get data from the user in the console using argument-less input()."""
try:
    list = []
    while True:
        number = int(input("Enter a number: "))
        if number == 0:
            sum = max(list) + min(list)
            average = sum / 2
            print(sum)
            print(average)
            break
        else:
            list.append(number)
except:
    print("Please enter numerical values!")