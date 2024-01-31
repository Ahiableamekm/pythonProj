 #This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import datetime as dt
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

ORIGIN_CITY_CODE = "LON"

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

tomorrow = dt.datetime.now() + dt.timedelta(hours=24)
six_month_from_today = dt.datetime.now() + dt.timedelta(hours=6*30)
data_sheet = data_manager.get_sheet_data()["prices"]

for row, city in enumerate(data_sheet, 2):
    if city["iataCode"] == "":
        code = flight_search.get_iata(city["city"])
        data_manager.update_sheet_data(code, row)


for destination in data_sheet:
    flight = flight_search.search_flights(origin_city_code=ORIGIN_CITY_CODE, 
                                 destination_city_code=destination["iataCode"],
                                 from_time=tomorrow,
                                 to_time=six_month_from_today)
    if flight.price < destination["lowestPrice"]:
        notification_manager.send_messsage(
            message=f"""Low price alert! Only £{flight.price} 
            to fly from {flight.origin_city}-{flight.origin_airport} 
            to {flight.destination_city}-{flight.destination_airport}, 
            from {flight.out_date.strftime("%Y-%m-%d")} 
            to {flight.return_date.strftime("%Y-%m-%d")}."""
        )