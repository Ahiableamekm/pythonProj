from dotenv import dotenv_values
import datetime as dt
import requests
from flight_data import FlightData


cred = dotenv_values(".env")
TEQUILA_API_KEY = cred["TEQUILA_API_KEY"]
ENDPOINT ="https://api.tequila.kiwi.com"


class FlightSearch:
    """This class is responsible for talking to the Flight Search API."""

    def __init__(self):
        self.header ={"apikey":TEQUILA_API_KEY}
      
    def get_iata(self, city):
        params = {
            "term":city,
            "location_types":"city",
            "limit":1,
        }
        response = requests.get(url=f"{ENDPOINT}/locations/query", params=params, headers=self.header)
        
        return response.json()["locations"][0]["code"]
    

    def search_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        search_input = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"}
        response = requests.get(url=f"{ENDPOINT}/search", params=search_input, headers=self.header)
        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            return None
        
        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=dt.datetime.utcfromtimestamp(data["route"][0]["dTime"]),
            return_date=dt.datetime.utcfromtimestamp(data["route"][1]["dTime"])
        )
        print(f"{flight_data.destination_city}: £{flight_data.price}")
        return flight_data
    