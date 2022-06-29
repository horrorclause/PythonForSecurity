"""
Labs for Class 3
"""

############
# Lab 1
############

upper_bound = int(input("Choose the range upper bound: ")) # Ask user for range upper limit

# iterate through the range specified
for x in range(1, upper_bound):
    print(f"The next number in the line is: {x}")



############
# Lab 2
############
# Create 1 list with 7 Classrooms with 10 students each ex. [[0,1,2,3,..], [0,1,2,3,...]]

classroom = []  # Empty list to store our 7 Classrooms

for i in range(7):  # Will create one classroom each iteration
    classroom.append([])  # Adds an empty list
    for students in range(1, 11):  # Adds 10 students to the classroom added during this iteration
        classroom[i].append(students)


# Using enumerate can help us count out the 7 classrooms. Using "start" lets us begin counting at 1 instead of 0
for iteration, c in enumerate(classroom, start=1):
    print(f"Class #{iteration} is {c}")



############
# Lab 3
############

counter = 0

while counter < 10:
    counter += 1
    if counter == 6:
        print("Found")
        break

    else:
        print(f"Check {counter}")


############
# Lab 4
############

servicePorts = {}

while True:
    service = input("Please enter a service's name or type '0' to stop: ")
    if service == "0":
        print("Stopping...")
        break

    port = input("Please enter a port number or type '0' to stop: ")
    if port == "0":
        break

    servicePorts[service] = port

print(servicePorts)


############
# Lab 5
############

money = 50
shopping_cart = []
fruits = {
    "Apple": 5,
    "Raspberry": 10,
    "Lemon": 20
}

while True:
    if money <= 0:  # Checks to see if you ran out of money
        print("Thanks for shopping with us!")
        break
    else:
        player_choice = input(f"Select a fruit {fruits}:\n").title()    # Ask the user to pick their fruit
        if player_choice in fruits:  # Check if the user selection is offered in fruits
            if money >= fruits[player_choice]:  # If the user has enough money, add the fruit to the cart
                shopping_cart.append(player_choice)
                money -= fruits[player_choice]  # Subtract the cost of the fruit from your shopping cart
                print(f"You have ${money} left.")
            else:
                print(f"You dont have enough money!\nYou only have ${money} left.\n")
        else:
            print("Invalid request")

print(f"Here is your shopping cart: {shopping_cart}.\n")

