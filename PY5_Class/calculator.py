#!/usr/bin/python3
"""
Py5 Lab 1
"""
first_num = int(input("Enter the first number: "))
second_num = int(input("Enter the second number: "))
operator = input("Enter one of the following operators: +, -, *, /: ")


def add(num1, num2):
    description = f"{num1} + {num2}"
    return f"The result of {description} = {num1+num2}"


def sub(num1, num2):
    description = f"{num1} - {num2}"
    return f"The result of {description} = {num1-num2}"


def mult(num1, num2):
    description = f"{num1} * {num2}"
    return f"The result of {description} = {num1*num2}"


def div(num1, num2):
    description = f"{num1} / {num2}"
    return f"The result of {description} = {num1/num2}"


def calc():
    allowed_calculations = {
        "+" : add,
        "-" : sub,
        "*" : mult,
        "/" : div
    }

    try:
        # Takes operater variable as input and feeds first and second num as inputs for the selected function
        result= allowed_calculations[operator](first_num, second_num)
        print(result)

    except KeyError:
        print("The parameters doesn't exist.")
    except ZeroDivisionError:
        print("Can't divide by 0.")


calc()
