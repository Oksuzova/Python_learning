import smtplib
import random
import datetime as dt

with open("quotes.txt") as file:
    quotes_fo_send = file.readlines()
    quote = random.choice(quotes_fo_send)

my_email = "testanya289@gmail.com"
password = "mjiphmycpctqztmv"

now = dt.datetime.now()
if now.weekday() == 0:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="42toks@gmail.com",
            msg=f"Subject: Quote for the day\n\n{quote}"
        )
