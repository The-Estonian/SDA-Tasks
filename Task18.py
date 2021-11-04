"""Write a program that encrypts a given string using the Caesar cipher, which is a special case of a mono-alphabetic substitution cipher. The program retrieves the text to be encrypted from the user and the number n by which the alphabet is moved by which the text is encrypted, and then prints the encrypted text in the console. For simplicity, it can be assumed that the input string consists only of lowercase letters of the English alphabet, i.e. 'a' - 'z' and spaces.

Example a: text: alice has a cat, n: 1, result: bmjdf ibt b dbu

Example b: text: alice has a cat, n: 26, result: alice has a cat

Get data from the user in the console using argument-less input()."""

#sentence = str(input("Please enter sentence to be encypted: "))
from typing import ValuesView


reconstruct = []
dissiminate = []
sentence = "randomness"
n = 5
alphabet = {
            1:"a", 
            2:"b", 
            3:"c", 
            4:"d", 
            5:"e", 
            6:"f", 
            7:"g", 
            8:"h",
            9:"i", 
            10:"j", 
            11:"k", 
            12:"l", 
            13:"m", 
            14:"n", 
            15:"o",
            16:"p", 
            17:"q", 
            18:"r", 
            19:"s", 
            20:"t", 
            21:"u", 
            22:"v", 
            23:"w", 
            24:"x", 
            25:"y", 
            26:"z"}

for _ in sentence:
    for key, value in alphabet.items():
        if value == _:
            dissiminate.append(key)
print(dissiminate)

