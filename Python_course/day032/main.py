# import smtplib
#
# my_email = "testanya289@gmail.com"
# password = "mjiphmycpctqztmv"
#
# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="42toks@gmail.com",
#         msg="Subject: Hello\n\nThis is the body of my email."
#     )
#


import datetime as dt

now = dt.datetime.now()

year = now.year
month = now.month
day = now.day
day_of_week = now.weekday()
print(day_of_week)

day_of_birth = dt.datetime(year=1995, month=12, day=15, hour=4)
