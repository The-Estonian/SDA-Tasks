"""Write a program that checks if the brackets are correctly matched in the user-specified arithmetic expression. The expression is given as a single string.

If the brackets are correctly paired, the program should write to the console the message: "OK". Otherwise, the program should write to the console the message: "Incorrect pairing of brackets".

Example a: 2 * (3.4 - (-7) / 2) * (a-2) / (b-1))) result: Incorrect pairing of brackets         

Example b: (2 * (3.4 - (-7) / 2) * (a-2) / (b-1)), result: OK

Example c: ") 2 * 4 (", result: Incorrect pairing of brackets

Get data from the user in the console using argument-less input()."""

while True:
    # input = input()
    #input = "2 * (3.4 - (-7) / 2) * (a-2) / (b-1)))"
    input = "(2 * (3.4 - (-7) / 2) * (a-2) / (b-1))"
    #input = "Today i saw ) and then (" + str(2 + 0)
    #input = ")This is not the correct way of doing things("
    left = 0
    right = 0
    
    for i in input:
        right = input.count(")")

        if right > left:
            print("Incorrect pairing of brackets BREAK")
            print(left, right)
            break

        left = input.count("(")
        if left == right:
            print("OK")
        if left != right:
            print("Incorrect pairing of brackets")

        print(left, right)
        