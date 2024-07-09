import random
guessTaken=0
num=random.randint(1,20)
print("I am guessing a number between 1 and 20")

for guessTaken in range(1,7):
    print('Guess a number: ')
    guess=int(input())
    if guess>num:
        print('Your guess is too high')
    elif guess<num:
        print("Your guess is too low")
    else:
        break

if guess==num:
    print("You guess the number in", guessTaken)
else:
    print("The number was ",num)