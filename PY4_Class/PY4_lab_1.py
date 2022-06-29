#!/usr/bin/python3

"""
Lab#1: Try & Except Practice
"""

try:
    num1 = int(input("Please enter a number: "))
    num2 = 0
    div = num1/num2
    print(div)
except ZeroDivisionError:
    print("Can't calculate it.")
except ValueError:
    print("Something went wrong!")