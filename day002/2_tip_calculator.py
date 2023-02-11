print("Welcome to the tip calculator.")

bill = input("What was the total bill? $")
percent = input("What percentage tip would you like to give? 10, 12 or 15? ")
people = input("How many people to split the bill? ")

result = float(bill)/int(people)*(1 + (float(percent)/100))

print(f"Each person should pay ${result:.2f}")