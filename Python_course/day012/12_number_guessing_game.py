import random


print("Welcome to the Number Guessing Game!")
print("I`m thinking of a number between 1 and 100")

num = random.choice(list(range(1, 101)))

if input("Choose a difficulty. Type 'easy' or 'hard': ") == "hard":
    lives = 5
else:
    lives = 10

print(f"You have {lives} attempts remaining to guess the number")
guess = int(input("Make a guess: "))

while lives != 0:
    if guess > num:
        print("Too high.")
    elif guess < num:
        print("Too low.")
    else:
        print(f"You got it! The number was {num}")
        break
    lives -= 1
    print(f"You have {lives} attempts remaining to guess the number")
    guess = int(input("Guess again: "))

if lives == 0:
    print("You lose...")

