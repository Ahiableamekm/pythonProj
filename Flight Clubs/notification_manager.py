import smtplib
from dotenv import dotenv_values

cred = dotenv_values(".env")
SENDER_EMAIL= cred["SENDER_EMAIL"]
SENDER_PASSWORD=cred["SENDER_PASSWORD"]

class NotificationManager:

    def send_sms(self, message, customer):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=SENDER_EMAIL, password=SENDER_PASSWORD)
            connection.sendmail(
                from_addr=SENDER_EMAIL,
                to_addrs=customer,
                msg=message)
            connection.close()
        
