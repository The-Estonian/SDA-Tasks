"""Write a program that receives text from the user and then creates a string that is the inverted text and displays it in the console.

For example, for the text Cat, the program should write the text taC in the console.

Get data from the user in the console using argument-less input()."""
while True:
    sentence = str(input("Enter text to be inversed: "))
    print("Enter X to exit program.")
    if sentence == "X":
        break
    answer = sentence[::-1]
    print(answer)