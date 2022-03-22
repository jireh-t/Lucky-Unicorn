"""LU Yes/No
Simplifies the input by converting it to lower case. Also accepts y or n as
abbreviations. Prints result of user choice as well as input - for testing
"""

# Ask the user if they have played before
played_before = input("Have you played this game before? ").lower()

# If they say yes, output 'Program Continues'
if played_before == "y" or played_before == "yes":
    print("Program continues")

# If they say no, output 'Display Instructions'
elif played_before == "n" or played_before == "no":
    print("Instructions below")

# Otherwise - show error
else:
    print("Please answer 'y' or 'n'")

print(f"You entered '{played_before}'")
