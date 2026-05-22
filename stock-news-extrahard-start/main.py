import os

import requests
from dotenv import load_dotenv
import datetime
import os
from twillo import send_sms

load_dotenv()

API_KEY = os.getenv("STK_PRICE_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# STOCK = "TMPV.BSE"
# COMPANY_NAME = "Tata Motors Passenger Vehicles"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").


baseurl="https://www.alphavantage.co/query"
parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": API_KEY,
}

response = requests.get(url=baseurl, params=parameters, timeout=10)
response.raise_for_status()
response.encoding = "utf-8"
response_json = response.json()

yesterday_date = str(datetime.date.today() - datetime.timedelta(days=1))
daybeforeyesterday_date = str(datetime.date.today() - datetime.timedelta(days=2))

yesterday_close = float(response_json["Time Series (Daily)"][yesterday_date]["4. close"])
daybeforeyesterday_close = float(response_json["Time Series (Daily)"][daybeforeyesterday_date]["4. close"])

difference = yesterday_close - daybeforeyesterday_close
percentage_change = (difference / yesterday_close) * 100

print(yesterday_close,daybeforeyesterday_close,difference,percentage_change)

if percentage_change > 5 or percentage_change < -5 or True:
    print("get news")

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
    news_baseurl = "https://newsapi.org/v2/top-headlines"
    parameters = {
        "q" : COMPANY_NAME,
        "apiKey" : NEWS_API_KEY
    }
    response = requests.get(url=news_baseurl, params=parameters, timeout=10)
    response.raise_for_status()
    response.encoding = "utf-8"
    response_json = response.json()
    articles = response_json["articles"]
    news = ""
    count = 0
    for article in articles:
        count += 1
        news += "News " + str(count) + ": \n"
        news += "Title : " + article["title"]+ "\n"
        news += "Description : " + article["description"] + "\n"
        if count >= 3:
            break


## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.
#BODY FORMATTING

    body = f"""
    CHANGE IN TSLA : {difference}
    NEWS UPDATE:
    {news}"""

    send_sms(body)

#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

