"""
Lab3: Handling Files

Part 1 of 2 files. This file creates the "test" file
"""

try:
    with open("text.txt", "r") as text:
        text.write("test")
except Exception as e:
    print("Unsupported Operation, cannot write in read mode.")
    print(e)



