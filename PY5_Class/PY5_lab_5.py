#!/usr/bin/python3
"""
Py5 Lab 5
"""

import random


def generate_random():
    number = random.randint(1,10)   # Creates a random number between 1 and 10
    return number


def main():
    random_number = generate_random()
    guessed_number = int(input("Guess a number between 1 and 10: "))

    if guessed_number is random_number:
        print("You got it!")

    else:
        print("Wrong!")
        print(f"It was {random_number}")


if __name__ == "__main__":
    main()
