import random
from hangman_arts import stages
from hangman_words import word_list

underscores = list()
lives = 6
chosen_word = random.choice(word_list)

for i in range(len(chosen_word)):
    underscores.append("_")

while "_" in underscores:
    cust_letter = input("Please, guess a letter: ").lower()

    print("\n" * 80)

    if cust_letter in underscores:
        print(f"You've already guessed {cust_letter}")

    for position, letter in enumerate(chosen_word):
        if letter == cust_letter:
            underscores[position] = letter
    print(underscores)

    if "_" not in underscores:
        print("You win!")

    if cust_letter not in chosen_word:
        print(f"You guessed {cust_letter}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            print("You lose...")
            print(stages[lives])
            break

    print(stages[lives])
