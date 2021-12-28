name = print("Type your name: ")

print("Welcome", name, "to this adventure!")

answer = input("You are on a dirt road, you can go left or right. which way will you go? ").lower()

if answer == "left":
    answer = input("You come to a river, you can walk around it or swim across? Type walk to walk around, or swim to swim across? ")

    if answer == "swim":
        print("You swim across and you were eaten by an aligator.")
    elif answer == "walk":
        print("You walked for many miles, you ran out of water and you lost the game.")
    else:
        print("Not a valid option. You lose.")
elif answer == "right":
    pass
else:
    print("Not a valid option. You lose.")