import random
import pandas
import datetime as dt
import smtplib

my_email = "testanya289@gmail.com"
password = "mjiphmycpctqztmv"

data = pandas.read_csv("birthdays.csv")
data_dict = data.to_dict(orient="records")

now = dt.datetime.now()
current_day = now.day
current_month = now.month

num = random.choice(range(1, 3))
letter = f"letter_templates\letter_{num}.txt"

for key in data_dict:
    if key["day"] == current_day and key["month"]:
        new_name = key["name"]
        with open(letter, "r") as f:
            name = f.read()
            new_letter = name.replace("[NAME]", new_name)

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="42toks@gmail.com",
                msg=f"Subject:Happy Birthday\n\n{new_letter}"
            )
