#!/usr/bin/python3

"""
Lab2: Error Handling
"""

product = 1

for i in range(4):  # Will iterate 4 times
    try:
        num = int(input("Enter a number: "))
        product *= num  # Increments up by the result of product * num
    except:
        print("The input is not a valid number.")

print(f"The final product is {product}! ")  # Using string formatting we do not need to convert the
                                            # variable to a string.


