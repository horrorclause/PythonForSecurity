#!/usr/bin/python3
"""
Codewars: Convert string to camel case
"""


def to_camel_case(text):

    newList = []

    try:

        for i in text:
            if i.isalpha():  # Checks to see if each character in the string is alpha
                newList.append(i)  # If it is, it gets appended as-is
            else:
                newList.append(" ")  # If it's not alpha, append a blank space

        redoneString = "".join(newList)  # Joins the list into a string
        redoneString = redoneString.title().replace(" ", "")  # Removes spaces

        if text[0].islower():  # If the first character of the original string is lower, keep it that way.
            redoneString = list(redoneString)
            redoneString[0] = redoneString[0].lower()
            redoneString = "".join(redoneString)

    except IndexError:
        print("You didn't enter anything.")
        pass

    return redoneString


print(to_camel_case(input("Enter string to convert to camelCase:\n")))
