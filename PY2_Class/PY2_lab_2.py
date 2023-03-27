#!/usr/bin/python3

"""
Lab 2 Exercise
"""
# Create a new script that checks if users can legally purchase an alcoholic beverage

firstName = input("What is your first name? : ")  # Take user input for name
lastName = input("What is your last name? : ")
age = int(input("What is your age? : "))   # Take user input for age

print(f"Your name is {firstName} and you are {age} years old.")  # fstring formatting
#print("Your name is {}, and you are {} years old".format(firstName, age))  # .format formatting

# if-else statement to check age
if age >= 21:
    print("You can buy alcoholic beverages")
else:
    print('Sorry you are too young to buy alcohol')
