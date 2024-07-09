import websocket
import json
import threading
import time
import datetime as dt
import requests


timestamps = []
prices = []
currentDay = None
openPosition = False
startingCash = 10
cash = startingCash
buyAmount = 0
buyPrice = 0
percentageChange = 0

wsUrl = "wss://ws.finnhub.io?token=cokf2gpr01qq4pkujt6gcokf2gpr01qq4pkujt70"
backend_url = "http://127.0.0.1:8000/stockllm/"
backend_start_cash_url = "http://127.0.0.1:8000/cash/2/"
backend_data = "http://127.0.0.1:8000/tradeprice/"

current_price_interval = 5  

def fetch_stock_llm_data():
    try:
        response = requests.get(backend_url)
        if response.status_code == 200:
            stock_data = response.json()
            return stock_data
        else:
            print(f"Error fetching data. Status code: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"HTTP request error: {e}")
        return None

def fetch_starting_cash():
    global cash
    try:
        response = requests.get(backend_start_cash_url)
        if response.status_code == 200:
            cash_data = response.json()
            cash = float(cash_data['value'])
            print(f"Starting cash successfully fetched: {cash:.2f} USD")
        else:
            print(f"Error fetching starting cash. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"HTTP request error: {e}")

def update_cash(new_cash_value):
    try:
        response = requests.put(backend_start_cash_url, json={"value": new_cash_value})
        if response.status_code == 200:
            print(f"Cash successfully updated to {new_cash_value:.2f} USD")
        else:
            print(f"Error updating cash value. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"HTTP request error: {e}")

def post_trade_data(symbol, action, current_price, entry_price):
    try:
        data = {
            "symbol": symbol,
            "action": action,
            "currentPrice": current_price,
            "entryPrice": entry_price
        }
        response = requests.post(backend_data, json=data)
        if response.status_code == 201:
            print(f"Trade entry successfully created: {data}")
        else:
            print(f"Error creating trade entry. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"HTTP request error: {e}")

def send_current_price():
    global openPosition, buyPrice
    if openPosition and prices:
        current_price = prices[-1]  
        try:
            data = {
                "symbol": "AAPL",
                "action": "UPDATE",
                "currentPrice": current_price,
                "entryPrice": buyPrice
            }
            response = requests.post(backend_data, json=data)
            if response.status_code == 201:
                print(f"Current price update successfully sent: {current_price}")
            else:
                print(f"Error sending current price update. Status code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"HTTP request error: {e}")
        threading.Timer(current_price_interval, send_current_price).start()

def onMessage(ws, message):
    global currentDay, openPosition, cash, buyAmount, buyPrice, percentageChange
    data = json.loads(message)

    if 'data' in data and len(data['data']) > 0:
        trades = data['data']

        for trade in trades:
            timestamp = trade['t']
            price = trade['p']
            timestamps.append(dt.datetime.fromtimestamp(timestamp / 1000.0))
            prices.append(price)
         
            print(f"Live price: {price}")
            
            date = dt.datetime.fromtimestamp(timestamp / 1000.0).strftime('%Y-%m-%d')
          
            if date != currentDay:
                currentDay = date
                applyStrategy(timestamp, price)
            else:
                printCurrentPosition(price)

def onError(ws, error):
    print(error)

def onClose(ws):
    print("WebSocket closed")

def onOpen(ws):
    ws.send('{"type":"subscribe","symbol":"AAPL"}')

def websocketThread():
    ws = websocket.WebSocketApp(wsUrl, on_message=onMessage, on_error=onError, on_close=onClose)
    ws.on_open = onOpen
    ws.run_forever()

def startWebsocket():
    thread = threading.Thread(target=websocketThread)
    thread.start()

def applyStrategy(timestamp, price):
    global openPosition, cash, buyAmount, buyPrice, percentageChange

    date = dt.datetime.fromtimestamp(timestamp / 1000.0).strftime('%Y-%m-%d')
    stock_llm_data = fetch_stock_llm_data()

    if stock_llm_data:
       

        current_aapl_recommendations = [entry for entry in stock_llm_data if entry['stock'] == 'AAPL' and entry['datetime'].startswith(dt.datetime.now().strftime('%Y-%m-%d'))]

        for recommendation in current_aapl_recommendations:
            confidence = recommendation['confidence']
            advice = recommendation['advice']

            if confidence >= 70:
                if advice.upper() == 'BUY':
                    print(f"{timestamp}: Buy signal detected for AAPL {price}")
                    if not openPosition:
                        buyAmount = int(cash / price)
                        buyPrice = price
                        cash -= buyAmount * price
                        print(f"{timestamp}: Bought {buyAmount} shares at price {price}, balance: {cash:.2f} USD")
                        openPosition = True
                        post_trade_data("AAPL", "BUY", price, buyPrice)  
                          
                        threading.Timer(1200, sellPositions, args=[timestamp, price]).start()# 20 minutes = 1200 
                        send_current_price() 
                elif advice.upper() == 'SELL':
                    print(f"{timestamp}: Sell signal detected for AAPL {price}")
                    if openPosition:
                        percentageChange = ((price - buyPrice) / buyPrice) * 100
                        cash += buyAmount * price

                        print(f"{timestamp}: Sold {buyAmount} shares at price {price}, balance: {cash:.2f} USD, percentage change: {percentageChange:.2f}%")

                        update_cash(cash)  
                        post_trade_data("AAPL", "SELL", price, buyPrice) 

                        openPosition = False
                else:
                    print(f"{timestamp}: Hold")
    else:
        print(f"{timestamp}: No data received from backend route.")

def sellPositions(timestamp, price):
    global openPosition, cash, buyAmount, buyPrice, percentageChange

    if openPosition:
        percentageChange = ((price - buyPrice) / buyPrice) * 100
        cash += (buyAmount * price)

        print(f"{timestamp}: Sold all position at Price {price}, balance: {cash:.2f}  percentage change: {percentageChange:.2f}%")
        update_cash(cash)  

        post_trade_data("AAPL", "SELL", price, buyPrice)  
        openPosition = False

def printCurrentPosition(currentPrice):
    global openPosition, cash, buyAmount, buyPrice, percentageChange

    if openPosition:
        currentValue = buyAmount * currentPrice
        print(currentPrice)
        profitLoss = currentValue - (buyAmount * buyPrice)

        percentageChangeCurrent = (profitLoss / (buyAmount * buyPrice)) * 100

        print(f"Current position - Purchase price: {buyPrice:.2f}, Amount: {buyAmount}, Balance: {cash:.2f} USD, Current value: {currentValue:.2f} USD, Percentage: {percentageChangeCurrent:.2f}%")

def sellAllPositions():
    global openPosition

    if openPosition:
        print("Selling all positions...")
        sellPositions(dt.datetime.now(), prices[-1])  
        print("Sale successfully completed")

if __name__ == "__main__":
    fetch_starting_cash()  
    startWebsocket()
    threading.Timer(600, sellAllPositions).start() 

    time.sleep(35)  