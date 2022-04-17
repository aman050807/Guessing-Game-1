import random
print("Number Guessing game")
number = random.randint(1,9)
chances =0
print("Guess a number (Between 1 and 9)")

while chances < 5:
    guess=int(input("Enter your guess:  "))

    if guess== number:
        print("Congratulations You Won!!")
    elif guess<number:
        print("Your guess was two low ; Guess a number higher")
    else:
        print("Your guess is two high; Guess A number low")

if not chances <5:
    print("Oops,You Lose!! the number is",number)