import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

index = len(names) - 1
ch = random.randint(0, index)

print(f"{names[ch]} is going to buy the meal today!")

# alternative solution
# ch = random.choice(names)
# print(ch + " is going to buy the meal today!")