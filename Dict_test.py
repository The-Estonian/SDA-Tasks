"""word_dict = {}
clean_words = []

while True:
    sentence = str(input("Enter a sentence: "))
    if sentence == "X":
        break
    for word in sentence.split(" "):
        clean_words.append(word.lower().strip("?!.,*="))
    for words in clean_words:
        if words in word_dict.keys():
            word_dict[words] += 1
        else:
            word_dict[words] = 1
    for key, value in word_dict.items():
        print(key, "-", value)"""

dict = {}

# sentence = str(input("info: "))
sentence = "Word word word word not word not not word not word not word word word" 
for value in sentence.items():
    if value in dict.keys():
        dict[value] += 1
    else:
        dict[value] = 1

print(dict)
