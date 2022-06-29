#!/usr/bin/python3

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

