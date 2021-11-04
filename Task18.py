"""Write a program that encrypts a given string using the Caesar cipher, which is a special case of a mono-alphabetic substitution cipher. The program retrieves the text to be encrypted from the user and the number n by which the alphabet is moved by which the text is encrypted, and then prints the encrypted text in the console. For simplicity, it can be assumed that the input string consists only of lowercase letters of the English alphabet, i.e. 'a' - 'z' and spaces.

Example a: text: alice has a cat, n: 1, result: bmjdf ibt b dbu

Example b: text: alice has a cat, n: 26, result: alice has a cat

Get data from the user in the console using argument-less input()."""

#sentence = str(input("Please enter sentence to be encypted: "))
while True:

    sentence_back = ""
    reconstruct = []
    reconstruct_key = []
    disseminate = []
    sentence, n = str(input("Please enter a sentence to cyper: ")), int(input("Please enter a number for cypher complexity: "))
    #sentence = "alice has a cat"
    alphabet = {
                0:"a", 
                1:"b", 
                2:"c", 
                3:"d", 
                4:"e", 
                5:"f", 
                6:"g", 
                7:"h",
                8:"i", 
                9:"j", 
                10:"k", 
                11:"l", 
                12:"m", 
                13:"n", 
                14:"o",
                15:"p", 
                16:"q", 
                17:"r", 
                18:"s", 
                19:"t", 
                20:"u", 
                21:"v", 
                22:"w", 
                23:"x", 
                24:"y", 
                25:"z",
                100:" "}
# Iterating over each letter in sentence and applying letter key value to disseminate list.
    for _ in sentence:
        for key, value in alphabet.items():
            if value == _:
                disseminate.append(key)
# Iterating over each key value in disseminate list and applying "n" times value to key. Also ignoring "space" key value in process.
    for _ in disseminate:
        if _ == 100:
            reconstruct_key.append(_)
        else:
            if _+n > 25:
                reconstruct_key.append(_-26+n)
            else:
                reconstruct_key.append(_+n)
            
# Iterating over alphabet dictionary with new key values to find new letters and appending them into reconstruct list.
    for _ in reconstruct_key:
        for key, value in alphabet.items():
            if key == _:
                reconstruct.append(value)
# Iterating over reconstruct list and assimilating them to new sentences.
    for _ in reconstruct:
        sentence_back += _

    print(sentence_back)
    break
