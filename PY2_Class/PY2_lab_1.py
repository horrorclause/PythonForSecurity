#!/usr/bin/python3

"""
Lab 1 Exercise
"""
x_string = input("Enter 1st number:")  # Input first number as string
y_string = input("Enter 2nd number:")  # Input second number as string

print("Concatenated: ", x_string+y_string)  # Concatenate both strings


# Converting string inputs to integers
x = int(x_string)
y = int(y_string)

print("Sum: ", x+y)
print("Difference: ", x-y)
print("Multiplication: ", x*y)
print("Division: ", x/y)
print("Remainder: ", x % y)
