"""Write a program that reads the text entered by the user, and then for that text converts all comma occurrences to the text "-MAKARENA" and displays in the console.

For example, for the text Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. '', The program should write in the console Lorem ipsum dolor sit amet-MAKARENA consectetur adipiscing elit-MAKARENA sed to eiusmod tempor incididunt ut labore et dolore magna aliqua. "

Get data from the user in the console using argument-less input()."""
# Loop for testing
while True:
    try:
# Actual code to run.
        word = str(input("Please enter a word: "))
        new_word = word.replace(",","-MAKARENA")
        print(new_word)
        if word == "X":
            break
# Exceptions
    except:
        print("Please enter a sentence with a comma.")
        print("If u want to exit the program, please enter X")
        continue

