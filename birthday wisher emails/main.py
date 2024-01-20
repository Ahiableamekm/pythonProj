##################### Extra Hard Starting Project ######################
import pandas
import datetime as dt 
import smtplib
import random
from dotenv import dotenv_values

credential = dotenv_values(".env")
my_email = credential["SENDER_EMAIL"]
my_password = credential["SENDER_PASSWORD"]


df = pandas.read_csv("./birthdays.csv")

now = dt.datetime.now()
day = now.day
month = now.month

for index, row in df.iterrows():
    birth_month = row["month"]
    birth_day = row["day"]

    if birth_month == month and birth_day == day:
        
        with open(f"./letter_templates/letter_{random.randint(1, 3)}.txt") as letter:
            content = letter.read()
            message = content.replace("[NAME]", row["name"])

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=row["email"],
                                msg=f"Subject:Happy Birthday\n\n{message}")






