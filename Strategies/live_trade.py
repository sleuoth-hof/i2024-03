import websocket
import json
import threading
import time
import datetime as dt


exampleNews = [
    ("2016-06-30", """Expansion into energy storage: Tesla announced today its entry into the energy storage market with the launch of new home battery products. The move aims to capitalize on growing interest in renewable energy solutions and diversify Tesla's revenue streams beyond electric vehicles.""", 80, 'Buy'),
    ("2020-03-12", """Impact of global pandemic: Tesla warned today of potential disruptions to its supply chain and production activities due to the ongoing global pandemic. The announcement comes amid growing concerns about the economic impact of the pandemic on the automotive industry.""", 80, 'Hold'),
    ("2021-06-05", """Investigation into vehicle safety: Tesla's vehicle safety record came under scrutiny today following reports of multiple accidents involving its electric cars. The incidents reignited concerns about the effectiveness of Tesla's Autopilot feature and prompted regulatory investigations into the company's safety practices.""", 60, 'HOLD'),
    ("2022-04-15", """Battery technology breakthrough: Tesla unveiled today a breakthrough in battery technology that promises to significantly reduce the cost and improve the performance of electric vehicles. The innovation is expected to further solidify Tesla's competitive advantage in the electric vehicle market.""", 80, 'Buy'),
    ("2022-09-30", """Supply chain disruptions: Tesla warned today of ongoing supply chain disruptions that could impact its production and delivery timelines. The announcement comes amid global supply chain challenges exacerbated by the COVID-19 pandemic and geopolitical tensions.""", 50, 'Hold'),
    ("2023-08-17", """Regulatory investigation: Tesla disclosed today that it is under investigation by regulatory authorities for alleged safety issues related to its electric cars. The announcement adds to mounting regulatory scrutiny facing Tesla and raises concerns among investors about potential fines and legal liabilities.""", 70, 'Sell'),
    ("2024-06-26", """Partnership with major tech company: Tesla announced today a strategic partnership with a major technology company to develop next-generation electric vehicle technologies. The collaboration aims to accelerate innovation in the electric vehicle industry and drive sustainable transportation solutions.""", 80, 'Buy')
]


timestamps = []
prices = []
currentDay = None
openPosition = False
startingCash = 100000  
cash = startingCash   
buyAmount = 0         
buyPrice = 0
percentageChange = 0

 #finhub news
wsUrl = "wss://ws.finnhub.io?token=cokf2gpr01qq4pkujt6gcokf2gpr01qq4pkujt70"

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
         
            print(f"live price: {price}")
            
            date = dt.datetime.fromtimestamp(timestamp / 1000.0).strftime('%Y-%m-%d')
          
            if date != currentDay:
                currentDay = date
                applyStrategy(timestamp, price)
            else:
                printCurrentPosition(price)

def onError(ws, error):
    print(error)

def onClose(ws):
    print("WebSocket closed ")

def onOpen(ws):

  
    ws.send('{"type":"subscribe","symbol":"BINANCE:BTCUSDT"}')

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
    
 
    for newsDate, newsText, confidence, advice in exampleNews:
        if date == newsDate:
            print(f"{timestamp}: News foundet for the date ,News: - {newsText}")
            if confidence >= 70:  
                if advice == 'Buy':
                    print(f"{timestamp}: buy signal detectet {price}")
                    if not openPosition:

                        buyAmount = int(cash / price)  

                        buyPrice = price

                        cash -= buyAmount * price

                        print(f"{timestamp}: boght {buyAmount} shares at price {price},  balance: {cash:.2f} USD")
                        openPosition = True  
                        
                                        #timer only for the test to  30 seconds 
                        timer = threading.Timer(30, sellPositions, args=[timestamp, price])

                        timer.start()
                elif advice == 'Sell':

                    print(f"{timestamp}: Sell signal detected {price}")
                    if openPosition:
                       
                        percentageChange = ((price - buyPrice) / buyPrice) * 100
                       

                        cash += buyAmount * price
                        print(f"{timestamp}: Sold {buyAmount} shares at price {price}, balance: {cash:.2f} USD, percentage change: {percentageChange:.2f}%")
                        openPosition = False 
                else:

                    print(f"{timestamp}: Hold")
            break

def sellPositions(timestamp, price):

    global openPosition, cash, buyAmount, buyPrice, percentageChange

    if openPosition:
      
        percentageChange = ((price - buyPrice) / buyPrice) * 100
        print( "price"+price)

        print("amount"+buyAmount)
        cash += (buyAmount * price) #change to  dezimal  error in  price calculation 

        print(f"{timestamp}: Sold all positions {price},balance: {cash:.2f} USD, percentage change: {percentageChange:.2f}%")
        openPosition = False



def printCurrentPosition(currentPrice):
    global openPosition, cash, buyAmount, buyPrice, percentageChange

    if openPosition:
        currentValue = buyAmount * currentPrice

        profitLoss = currentValue - (buyAmount * buyPrice)

        percentageChangeCurrent = (profitLoss / (buyAmount * buyPrice)) * 100
        print(f"Current Position - Buy Price: {buyPrice:.2f}, Amount: {buyAmount},  balance: {cash:.2f} USD, Current value: {currentValue:.2f} USD, Percentage : {percentageChangeCurrent:.2f}%")

if __name__ == "__main__":
    startWebsocket()

    time.sleep(30)


