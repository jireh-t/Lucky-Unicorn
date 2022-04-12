"""Component 3 (random tokens) v3
Format currency
Ensure odds favour the house - 5% chance of unicorn and 30% chance for donkey
"""

import random

token = ["unicorn",
         "horse", "horse", "horse",
         "donkey", "donkey", "donkey", "donkey", "donkey", "donkey",
         "zebra", "zebra", "zebra"]

STARTING_BALANCE = 100
balance = STARTING_BALANCE

# Testing loop to generate 20 tokens
for item in range(500):
    display = random.choice(token)

    # Adjust balance
    if display == "unicorn":
        balance += 4
    elif display == "donkey":
        balance -= 1
    else:
        balance -= 0.5

# Output
print(f"Starting balance : ${STARTING_BALANCE:.2f}")
print(f"Final balance: ${balance:.2f}")


