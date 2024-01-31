from twilio.rest import Client
from dotenv import dotenv_values

cred = dotenv_values(".env")
ACCOUNT_SID=cred["ACCOUNT_SID"]
AUTH_TOKEN=cred["AUTH_TOKEN"]
TWILIO_NUMBER=cred["TWILIO_NUMBER"]
PERSONAL_NUMBER=cred["PERSONAL_NUMBER"]

class NotificationManager:
    """This class is responsible for sending notifications with the deal flight details."""
    def __init__(self):
        self.client = Client(username=ACCOUNT_SID, password=AUTH_TOKEN)


    def send_messsage(self, message):
        msg = self.client.messages.create(
            from_=TWILIO_NUMBER,
            to=PERSONAL_NUMBER,
            body=message
        )
        print(msg.sid)