#!/usr/bin/python3
"""
Codewars: Bit Counting
"""


def count_bits(n):
    binary = bin(n)
    nums = 0

    for i in binary:
        if i == "1":
            nums += 1

    return nums  # Faster is binary.count("1")

print(count_bits(int(input("Enter your number: "))))
