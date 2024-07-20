import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
API_KEY = "JKZ869E7GB4PWD8C"

TWILIO_SID = "AC0b1230365fc79c4c289233cbefacea48"
TWILIO_AUTH_TOKEN = "9864e2a87ee03a2f34b8706775d24684"
RECOVERY_CODE = "3PC8ZMRJEKYRPHLW2RZ6M31B"

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
#url = 'https://www.alphavantage.co/query?function=&symbol=TSLA&apikey=JKZ869E7GB4PWD8C'
stock_params = {
    'function': 'TIME_SERIES_DAILY',
    'symbol':STOCK_NAME,
    'apikey': 'API_KEY'
}
response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()['Time Series (Daily)']
data_list = [value for (key, value) in data.items()]

#Get the day before yesterday's closing stock price
yesterday_data = data_list[1]
yesterday_closing_data = float(yesterday_data["4. close"])
day_before_yesterday_data = data_list[0]
day_before_yesterday_closing_data = float(day_before_yesterday_data["4. close"])
#Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

difference = yesterday_closing_data-day_before_yesterday_closing_data
up_down = True
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"
#Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

diff_percent = (difference/day_before_yesterday_closing_data)*100
print(f"{diff_percent}%")
#If TODO4 percentage is greater than 5 then print("Get News").
if abs(diff_percent) > 1:

    NEWS_APIKEY = '5c3d66f9dbd6482ba95a2fb21de9057a'
    NEWS_ENDPOINT = 'https://newsapi.org/v2/everything'

    news_param = {
        'apikey' : NEWS_APIKEY,
        'qInTitle': COMPANY_NAME
    }

    news_response = requests.get(NEWS_ENDPOINT, params = news_param)
    articles = news_response.json()["articles"]


# if percentage > 5:

    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    three_articles = articles[:3]
    print(three_articles)
    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

    formatted_articles = [f"{STOCK_NAME}:{up_down}{diff_percent}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]

    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

#Create a new list of the first 3 article's headline and description using list comprehension.
    for article in formatted_articles:
        message = client.messages.create(
            from_='+14786665068',
            body=article,
            to='+821051107804'
        )
#Send each article as a separate message via Twilio.

#Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

