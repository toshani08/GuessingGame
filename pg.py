import random 
print("Guessing Number Game")
number = random.randint(1,9)
chances=0

print("Guess any number from 1 - 9")

while chances < 5:
    guess=int(input("Enter your number: "))
    if guess==number:
        print("Your Guess is right")
    elif guess>number:
        print("Guess a lower number")
    elif guess<number:
        print("Guess a higher number")
        chances+=1
    if not chances < 5:
        print("You lost the right number is:", number)

