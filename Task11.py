"""Write a program that takes an integer greater than 1 from the user and checks if the number is a prime number. In the case when this number is a prime number, the program will write a message '' Yes '' in the console, otherwise it will write a message '' No '' in the console.

If the user specifies a number less than or equal to 1, the program will write to the console the message: "I am interrupting work".   Get data from the user in the console using argument-less input()."""
try:
    number = int(input("Enter a number: "))
    if number > 1:
        for i in range(2, number // 2 + 1):
            if (number % i) == 0:
                print("No")
                break
        else:
            print("Yes")
    else:
        print("I am interrupting work")
except:
    print("Please enter a valid number!")