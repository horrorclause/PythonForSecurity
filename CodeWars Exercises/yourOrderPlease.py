#!/usr/bin/python3

"""
Codewars: Your Order Please!

Your task is to sort a given string. Each word in the string will contain a single number.
This number is the position the word should have in the result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the input string is empty, return an empty string.
The words in the input String will only contain valid consecutive numbers.

"""


def order(sentence):
    if sentence == "":
        return sentence
    else:
        newList = sentence.split()
        orderedList = ["" for x in range(len(newList))]

        for word in newList:
            for character in word:
                if character.isdigit():
                    orderedList[int(character)-1] = word

    return " ".join(orderedList)

