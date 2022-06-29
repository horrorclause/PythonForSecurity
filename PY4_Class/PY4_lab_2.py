#!/usr/bin/python3

"""
Lab2: Error Handling
"""

product = 1

for i in range(4):
    try:
        num = int(input("Enter a number: "))
        product *= num  # Increments up by the result of product * num
    except:
        print("")



