print("Welcome to Very Berry Quiz!")

playing = input("Do you want to play? ")

if playing.lower() != 'yes':
    quit()

print("Okay! Let's play!")
score = 0


answer = input("What berry has more benefits for our body frozen than fresh? ")
if answer.lower() == "blueberry":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What citrus fruit has more calcium than cow milk? ")
if answer.lower() == "orange":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What berry has more benefits for our body frozen than fresh? ")
if answer.lower() == "blueberry":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What berry has more benefits for our body frozen than fresh? ")
if answer.lower() == "blueberry":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")