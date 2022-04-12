"""Component 3 (random tokens) v2
Calculate user balance based on random selection of tokens
"""

import random

token = ["zebra", "horse", "unicorn","donkey"]
balance = 100

# Testing loop to generate 20 tokens
for item in range(20):
    display = random.choice(token)
    print(display, end='\t') # can wrap output, making it easier to screenshot

    # Adjust balance
    if display == "unicorn":
        balance += 4
    elif display == "donkey":
        balance -= 1
    else:
        balance -= 0.5

    # Output
    print(f"Token: {display}, Balance: {balance}")



