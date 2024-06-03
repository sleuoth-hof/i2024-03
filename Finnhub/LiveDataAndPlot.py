import websocket
import json
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import datetime as dt
import threading

timestamps = []
prices = []

ws_url = "wss://ws.finnhub.io?token=cokf2gpr01qq4pkujt6gcokf2gpr01qq4pkujt70"

def on_message(ws, message):
    print("received   message:", message) 
    data = json.loads(message)
    if 'data' in data and len(data['data']) > 0:
        trades = data['data']
        for trade in trades:
            timestamp = trade['t']
            price = trade['p']
            timestamps.append(dt.datetime.fromtimestamp(timestamp / 1000.0))
            prices.append(price)
            print("Appended data poients", dt.datetime.fromtimestamp(timestamp / 1000.0), price)
            update_plot(None, timestamps, prices)

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    ws.send('{"type":"subscribe","symbol":"BINANCE:BTCUSDT"}')

def websocket_thread():
    ws = websocket.WebSocketApp(ws_url, on_message=on_message, on_error=on_error, on_close=on_close)
    ws.on_open = on_open
    print("Connect to WebSocket")
    ws.run_forever()


websocket_thread = threading.Thread(target=websocket_thread)
websocket_thread.start()

def update_plot(frame, timestamps, prices):
    print("Updating plot with {} data ".format(len(timestamps)))
    plt.clf()
    plt.plot(timestamps, prices)
    plt.title('Live BTC Price ')
    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.gcf().autofmt_xdate()

ani = animation.FuncAnimation(plt.gcf(), update_plot, fargs=(timestamps, prices), interval=10000, cache_frame_data=True)


plt.show()
