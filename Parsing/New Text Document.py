import requests
from datetime import datetime

def save_to_file(data):
    with open('fear_and_greed_index.txt', 'a') as file:
        file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')},{data}\n")

def send_to_lisa(data):
    lisa_endpoint = 'https://lisa-service.com/api/data'
    lisa_api_key = 'your_lisa_api_key'
    response = requests.post(lisa_endpoint, json={'data': data}, headers={'Authorization': f'Bearer {lisa_api_key}'})
    if response.status_code == 200:
        print("Data sent to LISA successfully.")
    else:
        print(f"Failed to send data to LISA: {response.status_code}")

api_key = 'your_api_key'
api_secret = 'your_api_secret'
url = 'https://api.binance.com/sapi/v1/market/spotData/fear_greed_index'

response = requests.get(url, headers={'X-MBX-APIKEY': api_key})

if response.status_code == 200:
    data = response.json()
    fear_and_greed_index = data['fearAndGreedIndex']
    print(f"Fear and Greed Index: {fear_and_greed_index}")
    save_to_file(fear_and_greed_index)
    send_to_lisa({'fear_and_greed_index': fear_and_greed_index})
else:
    print(f"Failed to retrieve data: {response.status_code}")
