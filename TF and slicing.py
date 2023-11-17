# True/False and slicing
# Brayden Towner
# 11/16/2023

greeting = input("Hello! (Hint: say hello back) >  ")
# Using lower (we did learn this) to make comparisons easier
if greeting.lower() == "hello":
    # Just a silly, not actually making an rpg out of this
    print("How are you? TODO: FINISH EPIC RPG")
else:
    print("You could at least say HELLO!")

# Can't write a funny that fast
ing_check = input("Just write a word with \"ing\" at the end >  ")

if ing_check[-3:].lower() == "ing":
    print("Thank you!")
else:
    print(">:(")