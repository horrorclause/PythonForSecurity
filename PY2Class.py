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


"""
Lab 2 Exercise
"""
# Create a new script that checks if users can legally purchase an alcoholic beverage

name = input("What is your name? : ")
age = int(input("What is your age? : "))

print(f"Your name is {name} and you are {age} years old.")
print("Your name is {}, and you are {} years old".format(name, age))
