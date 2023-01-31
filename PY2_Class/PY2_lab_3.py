#!/usr/bin/python3

"""
Lab 3 Exercise
"""
# Write code that asks the user to provide a score for an exam as input and checks what grade
# the score is associated with.

try:
    grade = int(input("Enter a grade: "))  # Grade is converted to an integer
    # if statement to check is 90 or greater
    if grade >= 90:
        print("A")
    elif grade >= 80:
        print("B")
    elif grade >= 70:
        print("C")
    elif grade >= 65:
        print("D")
    elif grade >= 0:
        print("F")

except ValueError:
    print("ERROR: Grades cannot be negative numbers, floats, or words.")
