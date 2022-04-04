"""Component 2 (how much) v1
Ask user how much they want to play with and check that the input is a valid
integer between 1 and 10. If it is, this amount becomes the balance in their
account """

user_balance = int(input("How much money would you like to play with? (Must "
                         "be an integer between 1 and 10) $"))

# Keep asking until a valid amount (1-10) is entered
while not 1 <= user_balance <= 10:
    print("Try again. Please enter a whole number between 1 and 10")
    # ask user for input
    user_balance = int(input("How much do you want to play with $"))

print(f"You are playing with ${user_balance}")





