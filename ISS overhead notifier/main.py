import datetime as dt
import time
import smtplib
import requests
from dotenv import dotenv_values

config = dotenv_values(".env")
MY_EMAIL = config["EMAIL"]
MY_PASSWORD = config["PASSWORD"]

MY_LAT = 7.946527
MY_LNG = -1.023194

def ISS_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")

    data = response.json()

    longitude = float(data["iss_position"]["longitude"])
    latitude = float(data["iss_position"]["latitude"])

    return (MY_LAT - 5 >= latitude <= MY_LAT + 5) and (MY_LNG - 5 >= longitude <= MY_LNG + 5)

def is_night():
    parameters ={
        "lat":MY_LAT,
        "lng":MY_LNG,
        "formatted":0
    }

    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = dt.datetime.now().hour
    return (time_now >= sunset or time_now <= sunrise)


while True:
    time.sleep(60)
    if ISS_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, 
                                to_addrs=MY_EMAIL, 
                                msg="Subject:ISS Overhead\n\nThe ISS is above go out and see it!")