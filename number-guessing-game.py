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
print(r_number)

# includes also 11, needs start and stop arg
# print(r_number)
