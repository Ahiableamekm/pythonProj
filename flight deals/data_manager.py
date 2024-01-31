from dotenv import dotenv_values
import requests

cred = dotenv_values(".env")
SHEETY_TOKEN_BEARER = cred["SHEETY_BEARER_TOKEN"]
ENDPOINT = "https://api.sheety.co/e23c90814dcad5fbf3b0ed22e2e852c2/flightDeals/prices"


class DataManager:
    """This class is responsible for talking to the Google Sheet."""
    def __init__(self):
        self.header = {"authorization": f"Bearer {SHEETY_TOKEN_BEARER}"}


    def update_sheet_data(self, code, row_id):

        code_input = {
            "price" :{
                "iataCode":code
            }
        }
        response = requests.put(url=f"{ENDPOINT}/{row_id}", json=code_input, headers=self.header)
        print(response.text)

    def get_sheet_data(self):
        
        response = requests.get(url=ENDPOINT,headers=self.header)
        return response.json()