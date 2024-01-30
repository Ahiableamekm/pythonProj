import requests
from twilio.rest import Client
from dotenv import dotenv_values

cred = dotenv_values(".env")

account_sid = cred["account_sid"]
auth_token = cred["auth_token"]
OW_API_KEY = cred["api_key"]
sender_number = cred["twilio_number"]
receiver_number = cred["personal_number"]

url = "https://api.openweathermap.org/data/2.5/forecast?"

parameters = {
    "lat":1.182050,
    "lon":34.192430,
    "appid":OW_API_KEY,
    "cnt":4
}

response = requests.get(url, params=parameters)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if condition_code < 700:
        will_rain  = True
        


if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
            .create(
                    body="It's going to rain today, remember to bring an ☂️☔",
                    from_=sender_number,
                    to=receiver_number
                )  
    print(message.status)