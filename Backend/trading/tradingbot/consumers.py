import json
from channels.generic.websocket import WebsocketConsumer
from .finnhub_utils import get_stock_price

class StockPriceConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
    
    def disconnect(self, close_code):
        pass
    
    def receive(self, text_data):
        data = json.loads(text_data)
        ticker = data['ticker']
        price = get_stock_price(ticker)
        self.send(text_data=json.dumps({
            'ticker': ticker,
            'price': price
        }))
