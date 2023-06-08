import random

secret = random.randint(1,100)

guess = None
count = 5

while guess != secret and count!=0:
    guess = input(f"Type a number between 1 and 100. you have {count} guesses. ")
    if guess.isdigit():
        guess = int(guess)
    if guess == secret:
        print("Hurray!")
        break
    elif int(guess) != int(secret) and int(count)!=0:
        count -= 1
        if guess > secret:
            print("too high!")
        else:
            print("too low.")
if guess != secret:
    print(f"game over! the number was {secret}!")