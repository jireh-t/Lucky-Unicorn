"""Component 3 (random tokens) v1
Generates random choice of token in random order
"""

import random

token = ["zebra", "horse", "unicorn","donkey"]

# Testing loop to generate 20 tokens
for item in range(20):
    display = random.choice(token)
    print(display, end='\t') # can wrap output, making it easier to screenshot

