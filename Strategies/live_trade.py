import pandas as pd
import yfinance as yf
import finnhub
import datetime
import matplotlib.pyplot as plt
import json
import threading
from websocket import create_connection 

# Set up Finnhub client
finnhub_client = finnhub.Client(api_key="cokf2gpr01qq4pkujt6gcokf2gpr01qq4pkujt70")

# Set up Yahoo Finance client
yf.pdr_override()

def on_message(ws, message):
    data = json.loads(message)
    if 'data' in data and len(data['data']) > 0:
        for trade in data['data']:
            process_trade(trade)

def process_trade(trade):
    symbol = trade['s']
    price = trade['p']
    timestamp = trade['t']
    volume = trade['v']
    print(f"Received trade for {symbol}: Price: {price}, Volume: {volume}, Timestamp: {timestamp}")

def create_websocket():
    websocket_url = 'wss://ws.finnhub.io'
    websocket = create_connection(websocket_url)
    while True:
        message = websocket.recv()
        on_message(websocket, message)

websocket_thread = threading.Thread(target=create_websocket)
websocket_thread.start()

start_date = datetime.datetime(2016, 1, 1)
end_date = datetime.datetime(2024, 4, 1)

def get_historical_data(symbol, start_date, end_date):
    data = yf.download(symbol, start=start_date, end=end_date)
    return data

data = get_historical_data('TSLA', start_date, end_date)

try:
    news = pd.read_csv('Toutput.csv', parse_dates=True, index_col='Date')
except FileNotFoundError:
    print("File 'Toutput.csv' not found.")

confidence_threshold = 40
initial_cash = 100000
cash = initial_cash
shares = 0

def implement_strategy(trade):
    global cash, shares
    symbol = trade['s']
    price = trade['p']
    timestamp = trade['t']
    volume = trade['v']
    date = datetime.datetime.utcfromtimestamp(timestamp / 1000).strftime('%Y-%m-%d')
    if date in news.index:
        confidence = news.loc[date, 'Confidence']
        advice = news.loc[date, 'Advice']
        if confidence >= confidence_threshold:
            if advice == 'Buy' and cash > price:
                shares_to_buy = cash // price
                cash -= shares_to_buy * price
                shares += shares_to_buy
                print(f"Bought {shares_to_buy} shares of {symbol} at {price} on {date}")
            elif advice == 'Sell' and shares > 0:
                cash += shares * price
                print(f"Sold {shares} shares of {symbol} at {price} on {date}")
                shares = 0

while True:
    pass









