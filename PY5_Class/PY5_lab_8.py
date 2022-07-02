#!/usr/bin/python3
"""
Py5 Lab 8
Car Creation
"""


class Car:
    def __init__(self, color, windows_number, price):
        self.color = color
        self.windows_number = windows_number
        self.price = price


car1 = Car("red", 4, 10000)
car2 = Car('Black', 6, 25000)

#print(vars(car1)) prints out all attributes
print(car2.price)
print(car1.windows_number)