from dotenv import dotenv_values
import requests

cred = dotenv_values(".env")
BEARER_TOKEN = cred["SHEETY_BEARER_TOKEN"]
ENDPOINT = "https://api.sheety.co/e23c90814dcad5fbf3b0ed22e2e852c2/flightDeals"


class DataManager:

    def __init__(self):
        self.destination_data = {}
        self.user_data = {}
        self.header = {"authorization": f"Bearer {BEARER_TOKEN}"}

    def get_destination_data(self):
        response = requests.get(url=f"{ENDPOINT}/prices", headers=self.header)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(f"{ENDPOINT}/prices/{city['id']}", json=new_data,  headers=self.header)
            print(response.text)

    def update_user_data(self, firstname, lastname, email):
        user_data = {
            "user":{
                "firstName":firstname,
                "lastName":lastname,
                "email":email
            }
        }
        response = requests.post(url=f"{ENDPOINT}/users", json=user_data, headers=self.header)
        
    
    def get_user_data(self):
        response = requests.get(url=f"{ENDPOINT}/users", headers=self.header)
        data = response.json()
        self.user_data = data["users"]
        return self.user_data
