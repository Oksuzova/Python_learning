import random
from art import logo, vs
from game_data import data


def compare(a, b):
    if a['follower_count'] > b['follower_count']:
        return a
    else:
        return b


def choice(a, b, user_choice):
    if user_choice == "a":
        return a
    else:
        return b


def game(score):
    a = random.choice(data)
    b = random.choice(data)

    print(f"Compare A. {a['name']}, {a['description']} from {a['country']}")
    print(vs)
    print(f"Versus B. {b['name']}, {b['description']} from {b['country']}")

    user_choice = (input("Who has more followers? Type 'A' or 'B': ")).lower()

    while compare(a, b) == choice(a, b, user_choice):
        score += 1
        print("\n" * 50)
        print(logo)
        print(f"You`re right! Score is {score}")
        game(score)

    if compare(a, b) != choice(a, b, user_choice):
        print(f"You`re wrong... The final score is {score}")
        exit()


print(logo)
game(score=0)
