import random
guessTaken=0
num=random.randint(1,20)
print("I am guessing a number between 1 and 20")

for guessTaken in range(1,7):
    guess=int(input('Guess a number: '))
    if guess>num:
        print("Guess is too high")
    elif guess<num:
        print("Guess is too low")
    else:
        break

if guess==num:
    print("You guessed the number in ",guessTaken)
else:
    print("The number was ", num)