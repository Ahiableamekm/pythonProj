import smtplib
from dotenv import dotenv_values
import random
import datetime as dt

credential = dotenv_values(".env")
my_email = credential["SENDER_EMAIL"]
my_password = credential["SENDER_PASSWORD"]
recipient_email = credential["RECEIPIENT_EMAIL"]

with open('./quotes.txt', 'r', encoding="utf-8") as quotes_file:
    quotes_list = quotes_file.readlines()
    quotes_list = [quote.strip("\n") for quote in quotes_list]
   
week_day = dt.datetime.now().weekday()
monday = 0
if week_day == monday:
    quote = random.choice(quotes_list)
    print(quote)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
                            from_addr=my_email,
                            to_addrs=recipient_email,
                            msg=f"Subject:Saturday Motivational Quote\n\n{quote}".encode("utf-8"))
