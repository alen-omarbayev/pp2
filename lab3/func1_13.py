import random

chance = 1
greeting = str(input("Hello! What is your name?\n"))
rndm = random.randint(1, 20)

user_guess = int(input(f"Well, {greeting}, I am thinking of a number between 1 and 20.\nTake a guess.\n"))

if user_guess == rndm:
    print(f"Good job, {greeting}! You guessed my number in {chance} guesses!")
else:
    while user_guess != rndm:
        if user_guess < rndm:
            user_guess = int(input("Your guess is too low.\nTake a guess.\n"))
            chance += 1
        elif user_guess > rndm:
            user_guess = int(input("Your guess is too high.\nTake a guess.\n"))
            chance += 1
        elif user_guess == rndm:
            break
    print(f"Good job, {greeting}! You guessed my number in {chance} guesses!")
    