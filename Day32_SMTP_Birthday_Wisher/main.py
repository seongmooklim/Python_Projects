#
#

#
#

# connection.close()

# import datetime as dt
#
# now= dt.datetime.now()
# year = now.year
# day_of_week = now.weekday()
# print(day_of_week)
#
# date_of_birth = dt.datetime(year=1984, month=8, day=14)
# print(date_of_birth)
import random
import datetime as dt
import smtplib

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 2:

    my_email = "sm.lim.tta@gmail.com"
    password = "grqb whxy tvsn zcjq"

    with open('quotes.txt') as file:
        lines = file.readlines()
        quote = random.choice(lines)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="seongmook.lim@tta.or.kr",
                            msg=f"Subject: Quotes\n\n{quote}")

