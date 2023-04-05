#!/usr/bin/python3

"""
Lab#1: Try & Except Practice
"""

try:
    num1 = int(input("Please enter a number: "))
    num2 = 0
    div = num1/num2
    print(div)

except ZeroDivisionError:   # Use except blocks to catch errors for graceful error handling
    print("Can't calculate it.")
except ValueError:  # Catches the exception raised when using str instead of int in "num1"
    print("Something went wrong!")

except Exception:
    print("This is the generic Exception Block.")