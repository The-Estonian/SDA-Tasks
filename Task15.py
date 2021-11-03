"""Write a program that reads the text entered by the user and then divides it into individual words. Then counts the number of occurrences of words regardless of case and writes them to the console in alphabetical order.

For example, for the text 'Ala likes cats, but she is not liked by Cats.' ', The program should write in the console:

ala - 1
but - 1
is - 1
cats - 2
likes - 1
liked - 1
no - 1
through - 1
Assume that any punctuation marks may appear in the text.

Get data from the user in the console using argument-less input()."""
# Initialised dictionary and list.
word_dict = {}
cleaned = []

# Continuous loop to fill dictionary
while True:

# Sentence input code and program exit code
    print("Enter a sentence for counting.")
    print("To exit program enter X")
    sentence = str(input("Please enter a sentence: "))
    if sentence == "X":
        break

# Splitting sentence to words and cleaning out commas and cases.
    for each_word in sentence.split(" "):
        cleaned.append(each_word.lower().strip(".,_-!?"))

# Adding individual words to the dictionary
    for word in cleaned:
        if word in word_dict.keys():
            word_dict[word] += 1
        else:
            word_dict[word] = 1

# Sorting dictionary alphabetically into list before print iteration.
    word_dict_sorted = sorted(word_dict.items())

# Iterating over words, values in dictionary and printing them out.
    for x, y in word_dict_sorted:
        print(x, "-", y)
