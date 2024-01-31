import datetime as dt
import requests
from dotenv import dotenv_values

cred = dotenv_values(".env")
NUTRITIONIX_API_ID = cred["NUTRITIONIX_API_ID"]
NUTRITIONIX_API_KEY = cred["NUTRITIONIX_API_KEY"]
NUTRITIONIX_ENPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_BEARER_TOKEN = cred["SHEETY_BEARER_TOKEN"]
GOOGLE_SHEETY_ENPOINT = f"https://api.sheety.co/e23c90814dcad5fbf3b0ed22e2e852c2/workoutTracking/workouts"

header ={
    "x-app-id":NUTRITIONIX_API_ID,
    "x-app-key":NUTRITIONIX_API_KEY
}

nutrix_input = {
    "query":input("log your exercise details in: ")
}

response = requests.post(url=NUTRITIONIX_ENPOINT, json=nutrix_input, headers=header)
nutrix_data = response.json()["exercises"]

gshty_header = {
    "authorization": f"Bearer {SHEETY_BEARER_TOKEN}"
}

for exercise in nutrix_data:
    today = dt.datetime.now()
    sheet_input = {
        "workout":{
            "date":today.date().strftime("%d/%m/%Y"),
            "time":today.time().strftime("%H:%M:%S"),
            "exercise":exercise["name"],
            "duration":exercise["duration_min"],
            "calories":exercise["nf_calories"],
        }
    }

    gshty_response = requests.post(url=GOOGLE_SHEETY_ENPOINT, json=sheet_input, headers=gshty_header)
    print(gshty_response.text)
