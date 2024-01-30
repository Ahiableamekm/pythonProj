import requests
from dotenv import dotenv_values
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

cred = dotenv_values(".env")
ALPHAVANTAGE_API_KEY = cred['ALPHAVANTAGE_API_KEY']
NEWS_API_KEY = cred["NEWS_API_KEY"]
TWILIO_ACCOUNT_SID = cred["TWILIO_ACCOUNT_SID"]
TWILIO_AUTH_TOKEN = cred["TWILIO_AUTH_TOKEN"]
TWILIO_NUMBER = cred["TWILIO_NUMBER"]
RECEIVER_NUMBER = cred["RECEIVER_NUMBER"]

ALPHAVANTAGE_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

alphavantage_params = {
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK_NAME,
    "apikey":ALPHAVANTAGE_API_KEY
}


news_params = {
    "qInTitle":COMPANY_NAME,
    "from":"2024-01-24",
    "sortedby":"publishedAt",
    "apiKey":NEWS_API_KEY
}

response = requests.get(ALPHAVANTAGE_ENDPOINT, params=alphavantage_params)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
data_list = [value for key, value in data.items()]

yesterday_closing = float(data_list[0]["4. close"])
day_before_closing = float(data_list[1]["4. close"])

difference = (yesterday_closing - day_before_closing)
pct_change = round((difference/yesterday_closing) * 100)

upward = None
if difference > 0:
    upward ="🔺"
else:
    upward = "🔻"


if abs(pct_change) > 2:

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    news_data = news_response.json()["articles"]
    three_articles = news_data[:3]
    
    formatted_articles = [f"{STOCK_NAME}:{upward} {pct_change}%\nHeadline: {article['title']} \n\nBrief: {article['description']}" for article in three_articles]

    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    for article in formatted_articles:
        client.messages.create(
            to=RECEIVER_NUMBER,
            from_=TWILIO_NUMBER,
            body=article
            
        )



