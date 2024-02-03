import smtplib
import requests
from dotenv import dotenv_values
from bs4 import BeautifulSoup


cred = dotenv_values(".env")
EMAIL = cred["EMAIL"]
PASSWORD = cred["PASS"]
price_endpoint = input("what amazon product do you want to track? Please provide amazon webpage of the product: ") #"https://www.amazon.com/ERGOMAKER-Adjustable-Standing-Sit-Stand-SM205-140/dp/B09H59YB3Y/ref=sr_1_4_sspa?crid=2WXK79SF40LKQ&keywords=work%2Bdesk%2Bfor%2Bhome%2Boffice&qid=1706962121&sprefix=work%2Bde%2Caps%2C304&sr=8-4-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1"
price_target = float(input("what is your price target? ") )# 170.00


response = requests.get(price_endpoint)
product_webpage = response.text

soup  = BeautifulSoup(product_webpage, "html.parser")
product = soup.find(name="span", id="productTitle").getText().strip()
whole = soup.select_one("span.a-price-whole").getText()
deci = soup.select_one("div.aok-relative span.a-price span[aria-hidden='true'] span.a-price-fraction").getText()

product_price = float(whole + deci)


if product_price < price_target:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg=f"Subject: Amazon Price Alert!! \n\n{product} is now ${product_price} \n{price_endpoint}"
        )