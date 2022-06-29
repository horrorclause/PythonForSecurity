#!/usr/bin/python3
"""
Codewars: Convert string to camel case
"""


def to_camel_case(text):
    newList = []

    try:

        for i in text:
            if i.isalpha():
                newList.append(i)
            else:
                newList.append(" ")

        redoneString = "".join(newList)
        redoneString = redoneString.title().replace(" ", "")

        if text[0].islower():
            redoneString = list(redoneString)
            redoneString[0] = redoneString[0].lower()
            redoneString = "".join(redoneString)
    except:
        pass

    return redoneString

