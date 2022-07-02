#!/usr/bin/python3
"""
Py5 Lab 3
"""

global_variable = 5
changed_global_variable = 20


def local_change():
    global_variable = 10
    print(f"Inside function, global_variable is: {global_variable}")  # Only modifies variable within the function, not globally
    global changed_global_variable  # Calling global variable and modifying it
    changed_global_variable += 5       # Will change the value of the global variable
    print(f"Inside function changed_global_variable's value: {changed_global_variable}")


local_change()


print(f"Outside function global_variable's value: {global_variable}")
print(f"Outside function changed_global_variable's value: {changed_global_variable}")