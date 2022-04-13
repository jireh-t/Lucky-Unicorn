"""Based on 06_rounds_v2
Converting v2 into a function
"""

import random


# Function to generate random token
def generate_token(balance):

    rounds_played = 0
    play_again = ""

    # Testing loop to generate 5 tokens
    while play_again != "x":
        rounds_played += 1 # keep track of rounds
        number = random.randint(1,100) # Can only be a donkey

         # adjust balance
        # If the random number is between 1 and 5
        # User gets a unicorn (add $4 to balance)
        if 1 <= number <= 5:
            token = "unicorn"
            balance += 4

        # If the number is between 6 and 36
        # User gets a donkey (subtract $1 from balance)
        elif 6 <= number <= 36:
            token = "donkey"
            balance -= 1

        # In all other cases, the token must be a horse or zebra
        # (subtract $0.50 from the balance in either case)
        else:
            # if the number is even, set the token to zebra
            if number % 2 == 0:
                token = "zebra"
                balance -= 0.5

            # otherwise, set the token to horse
            else:
                token = "horse"
                balance -= 0.5
        # output
        print(f"Round {rounds_played}, Token: {token}, Balance ${balance:.2f}")
        if balance < 1:
            print()
            print("Sorry but you have run out of money")
            play_again = "x"
        else:
            print()
            play_again = input("Do you want to play another round\n<enter> to play again or 'X' to exit").lower()
    print()
    return(balance)


# Main Routine

starting_balance = 5
closing_balance = generate_token(starting_balance)
print(f"Thanks for playing")
print(f"You started with ${starting_balance:.2f}")
print(f"and leave with ${closing_balance:.2f}")
print(f"Goodbye!")

