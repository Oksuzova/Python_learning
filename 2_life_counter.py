# count how many days, weeks, and months of your life left
age = input("What is your current age? ")

days = 32850 - (int(age) * 365)
weeks = 4680 - (int(age) * 52)
months = 1080 - (int(age) * 12)

print(f"You have {days} days, {weeks} weeks, and {months} months left.")