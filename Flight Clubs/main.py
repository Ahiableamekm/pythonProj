from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager


data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

ORIGIN_CITY_IATA = "LON"

def send_deal(firstname, lastname, email):
    for destination in sheet_data:
        flight = flight_search.check_flights(
            ORIGIN_CITY_IATA,
            destination["iataCode"],
            from_time=tomorrow,
            to_time=six_month_from_today
        )
        try:
            if flight.price < destination["lowestPrice"]:
                notification_manager.send_sms(
                    message=f"Subject:Low price alert! \n\nDear {firstname} {lastname} \nOnly £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}.".encode("utf-8"),
                    customer = email
                )
        except AttributeError:
            return None

print("Welcome to pipythonme's Flight Club \nWe find the best flight deals and email you")
firstname = input("What is your first name?: ")
lastname = input("What is your last name?: ")
email = input("what is your email?: ")
email_confirmation = input("Type you email again: ")

if email == email_confirmation:
    data_manager.update_user_data(firstname, lastname, email)
else:
    print("Unmatched email, check your email")

sheet_data = data_manager.get_destination_data()

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()



tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

user_data = data_manager.get_user_data()
if len(user_data) > 0:
    for user in user_data:
        send_deal(user["firstName"], user["lastName"], user["email"])

else:
    print("No users!")



