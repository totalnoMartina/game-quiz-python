import random

top_of_range = input("Type a number: ")


if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please, type in number larger than zero next time")
        quit()
else:
    print("Please type a number next time.")
    quit()

r_number = random.randint(0, top_of_range)
guesses = 0

# includes also 11, needs start and stop arg
# print(r_number)
while True:
    guesses += 1
    user_guess = input("Take a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time.")
        continue

    if user_guess == r_number:
        print("You got it!")
        break
    else:
        if user_guess > r_number:
            print("You were above the number!")
        else:
            print("You were below the number!")
        


print("You got it in", guesses, "guesses")

