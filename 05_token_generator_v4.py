"""Component 3 (random tokens) v3
Calculate percentages to ensure the odds favour the house
5% unicorns, 30% donkeys, and the remaining 65% horses/zebras
"""

import random


STARTING_BALANCE = 100
balance = STARTING_BALANCE

# Testing loop to generate 20 tokens
for item in range(10):
    number = random.randint(1, 100)

    # Adjust balance
    # If the number is between 1 and 5
    # User gets a unicorn (add $4 to balance)
    if 1 <= number <= 5:
        token = "unicorn"
        balance += 4
    elif 6 <= number <= 36:
        token = "donkey"
        balance -= 1
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
    print(f"Token: {token}, Balance: {balance:.2f}")

print(f"Token: {token}, Balance: {balance:.2f}")
print(f"Starting balance : ${STARTING_BALANCE:.2f}")
print(f"Final balance: ${balance:.2f}")
