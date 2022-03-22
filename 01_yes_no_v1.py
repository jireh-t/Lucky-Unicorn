# Ask the user if they have played before
played_before = input("Have you played this game before? (y/n) ")

# If they say yes, output 'Program Continues'
if played_before == "y":
    print("Program continues")

# If they say no, output 'Display Instructions'
elif played_before == "n":
    print("Instructions below")

# Otherwise - show error
else:
    print("Please answer 'y' or 'n'")
