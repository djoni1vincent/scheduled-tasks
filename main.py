# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.

import smtplib
import datetime as dt
import pandas as pd
import random
import os

# import os and use it to get the Github repository secrets
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

now = dt.datetime.now()
today_day = now.day
today_month = now.month

df = pd.read_csv("birthdays.csv")
dict_csv = df.to_dict(orient="records")
birthsday_today = [person for person in dict_csv if person["day"] == today_day and person["month"] == today_month]

if birthsday_today:
    for person in birthsday_today:
        file = f"letter_templates/letter_{random.randint(1, 3)}.txt"
        with open(f"{file}", "r") as data:
            letter = data.read()
            format_letter = letter.replace("[NAME]", person["name"])

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
            connection.login(EMAIL, PASSWORD)
            connection.sendmail(
                from_addr=EMAIL,
                to_addrs=person["email"],
                msg=f"Subject:Happy Birthday\n\n{format_letter}"
            )
