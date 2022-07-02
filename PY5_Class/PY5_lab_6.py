#!/usr/bin/python3
"""
Py5 Lab 6
Recursive Search
"""

lst = [
    1,
    2,
    "a",
    [4, 5, "b", 6],
    [7,
        [8, "d", 9]
     ]
    ]


def print_numbers(item_list):
    for item in item_list:
        if type(item) == int:
            print(item)
        elif type(item) == list:
            print_numbers(item)


print(print_numbers(lst))