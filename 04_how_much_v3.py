"""Component 2 (how much) v3
More efficient method - includes valid range as the basis of the while loop
which eliminates the need to use the 'valid' variable"""

# Main routine
error = "That was not a valid input\n"
user_balance = 0

# keep asking until a valid amount (1-10) is entered
while not 1 <= user_balance <= 10:
    try:
            # ask for amount
        user_balance = int(input("Please enter a whole number between 1 and 10\n"
                                 "How much would you like to play for? $"))
        print()

    except ValueError:
        print(error)

print(f"You are playing with ${user_balance}")
