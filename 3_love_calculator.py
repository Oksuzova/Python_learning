print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

low_name1 = name1.lower()
low_name2 = name2.lower()

t = low_name1.count("t") + low_name2.count("t")
r = low_name1.count("r") + low_name2.count("r")
u = low_name1.count("u") + low_name2.count("u")
e = low_name1.count("e") + low_name2.count("e")

tr = str(t + r + u + e)

l = low_name1.count("l") + low_name2.count("l")
o = low_name1.count("o") + low_name2.count("o")
v = low_name1.count("v") + low_name2.count("v")
e = low_name1.count("e") + low_name2.count("e")

love = str(l + o + v + e)
total = int(tr+love)

if total < 10 or total > 90:
    print(f"Your score is {total}, you go together like coke and mentos.")
elif 40 < total < 50:
    print(f"Your score is {total}, you are alright together.")
else:
    print(f"Your score is {total}")
