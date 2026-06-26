import random

attempt = 0
random_integer = random.randint(1, 100)

guess = int(input("Guess a number between 1 to 100: "))
attempt += 1

while guess != random_integer:

    if guess < random_integer:
        condition = "higher"  
    else:
        condition = "lower"

    guess = int(input(f"Enter a {condition} number: "))
    attempt += 1


print(f"Congratulations! You guessed the number {random_integer} correctly in {attempt} attempts.")