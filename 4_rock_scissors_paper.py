import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

rsp = [rock, scissors, paper]

print("Welcome to the Rock-Scissors-Paper game!")
cust_choice = input("What do you choose? Enter 1 for rock, 2 for scissors, 3 for paper: ")
pc_choice = random.randint(1, 3)

try:
    cust_choice = int(cust_choice)
    if cust_choice == 0:
        print("You made the wrong choice... game over")
    else:
        print(rsp[cust_choice-1])
        print("Computer chose:\n" + rsp[pc_choice-1])

        if cust_choice == pc_choice:
            print("Looks like we have no winner... Friendship win!")
        elif cust_choice == 1 and pc_choice == 2 or cust_choice == 2 and pc_choice == 3 or cust_choice == 3 and pc_choice == 1:
            print("You win!")
        else:
            print("You lose...")
except:
    print("You made the wrong choice... game over")