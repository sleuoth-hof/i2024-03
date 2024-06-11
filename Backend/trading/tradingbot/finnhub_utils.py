# finnhub_utils.py
import finnhub

def get_stock_price(ticker):
    finnhub_client = finnhub.Client(api_key="cpk6guhr01qs6dmbtir0cpk6guhr01qs6dmbtirg")
    try:
        price = finnhub_client.quote(ticker)['c']
        return price
    except Exception as e:
        print(f"Error fetching price for {ticker}: {e}")
        return None
