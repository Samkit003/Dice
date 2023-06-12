import random

number = random.randint(1, 100)
guess = 0
count = 0

while guess != number:
    guess = int(input("Guess a number between 1 and 100: "))
    count += 1
    if guess > number:
        print("Too high!")
    elif guess < number:
        print("Too low!")

print("Congratulations! You guessed the number in", count, "tries.")
