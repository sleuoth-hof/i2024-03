from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import MarketNews 
from .models import StockRecommendation,Cache,Trade
from .serializers import MarketNewsSerializer
from .serializers import StockRecommendationSerializer
from .serializers import CacheSerializer
from .serializers import TradeingSerializer
from django.shortcuts import get_object_or_404
import finnhub
import websocket
import requests
import json
from .models import TradeSignal
from .serializers import TradeSignalSerializer

from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from .models import CSVFile
from .forms import CSVFileForm

def generate_graph(file_path):
    # Load CSV file into a DataFrame
    df = pd.read_csv(file_path)
    df["Date"] = pd.to_datetime(df["Date"])
    
    # Generate a simple graph using Seaborn (example: plot first column vs second column)
    plt.figure()
    sns_plot = sns.lineplot(x="Date",y="Open", data=df)
    graph_path = 'media/graph.png'
    sns.set_theme(style="darkgrid")
    sns_plot.figure.savefig(graph_path)
    plt.close()
    return graph_path

def index(request):
    graph_path = None
    if request.method == 'POST':
        form = CSVFileForm(request.POST)
        if form.is_valid():
            csv_file = form.cleaned_data['csv_file']
            graph_path = generate_graph(csv_file.file_path)
    else:
        form = CSVFileForm()
    return render(request, 'index.html', {'form': form, 'graph_path': graph_path})

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def test(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())

class MarketNewsView(APIView):
    def get(self, request):
        category = request.query_params.get('category')
        min_id = request.query_params.get('minId', 0)
      
        finnhub_client = finnhub.Client(api_key="cokf2gpr01qq4pkujt6gcokf2gpr01qq4pkujt70")
        news = finnhub_client.general_news(category, min_id=min_id)
        
        for item in news:
            news_id = item['id']
            obj, created = MarketNews.objects.get_or_create(
                news_id=news_id,
                defaults={
                    'category': item['category'],
                    'datetime': item['datetime'],
                    'headline': item['headline'],
                    'image': item['image'],
                    'related': item['related'],
                    'source': item['source'],
                    'summary': item['summary'],
                    'url': item['url']
                }
            )
            if not created:
                obj.category = item['category']
                obj.datetime = item['datetime']
                obj.headline = item['headline']
                obj.image = item['image']
                obj.related = item['related']
                obj.source = item['source']
                obj.summary = item['summary']
                obj.url = item['url']
                obj.save()

        market_news = MarketNews.objects.all()
        serializer = MarketNewsSerializer(market_news, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class ProcessNewsView(APIView):
    def get(self, request):
        all_market_news = MarketNews.objects.all()
        print(all_market_news)
        for news in all_market_news:
            print(news)
            prompt =  "tesxst"

            url = 'http://54.160.119.237:11434/api/generate'
            data = {
                "model": "stockLLM",
                "prompt": prompt,
                "format": "json",
                "stream": False
            }

            response = requests.post(url, json=data)

            if response.status_code == 200:
                clean_response = response.json()['response'].strip()
                filter_response = json.loads(clean_response)
                
                for item in filter_response:
                    print(item)
                    StockRecommendation.objects.create(
                        stock=item['stock'],
                        confidence=item['confidence'],
                        advice=item['advice']
                    )
            else:
                return Response({"error": "Fehler bei der Anfrage. Statuscode: {}".format(response.status_code)}, status=400)
        
        return Response({"message": "Daten erfolgreich verarbeitet und gespeichert."}, status=200)

    def get(self, request):
        recommendations = StockRecommendation.objects.all()
        serializer = StockRecommendationSerializer(recommendations, many=True)
        return Response(serializer.data)
    
class CacheView(APIView):
    def get(self, request, pk=None):
        if pk is not None:
            cache_obj = get_object_or_404(Cache, pk=pk)
            serializer = CacheSerializer(cache_obj)
            return Response(serializer.data)
        else:
            caches = Cache.objects.all()
            serializer = CacheSerializer(caches, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = CacheSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        cache_obj = get_object_or_404(Cache, pk=pk)
        serializer = CacheSerializer(cache_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
'''
class TradeWebSocket(APIView):
    def get(self, request):
        trade_data = []

        def on_message(ws, message):
            data = json.loads(message)
            if 'type' in data and data['type'] == 'trade':
                trades = data.get('data', [])
                for trade in trades:
                    symbol = trade.get('s', '')
                    last_price = trade.get('p', '')
                    timestamp = trade.get('t', '')
                    volume = trade.get('v', '')
                    trade_data.append({
                        'symbol': symbol,
                        'last_price': last_price,
                        'timestamp': timestamp,
                        'volume': volume
                    })
            elif 'type' in data and data['type'] == 'ping':
                print("Received ping from server.")
            else:
                print("Received unknown message.")

        def on_error(ws, error):
            print(error)

        def on_close(ws):
            print("### closed ###")

        def on_open(ws):
            print("WebSocket connection opened.")
            ws.send('{"type":"subscribe","symbol":"AAPL"}')
           

        websocket.enableTrace(True)
        ws = websocket.WebSocketApp(
            "wss://ws.finnhub.io?token=cokf2gpr01qq4pkujt6gcokf2gpr01qq4pkujt70",
            on_message=on_message,
            on_error=on_error,
            on_close=on_close
        )
        ws.on_open = on_open
        ws.run_forever()

        return Response(trade_data, status=status.HTTP_200_OK)
'''
class StockRecommendationView(APIView):
    def get(self, request, pk=None):
        if pk is not None:
            stock_recommendation = get_object_or_404(StockRecommendation, pk=pk)
            serializer = StockRecommendationSerializer(stock_recommendation)
            return Response(serializer.data)
        else:
            stock_recommendations = StockRecommendation.objects.all()
            serializer = StockRecommendationSerializer(stock_recommendations, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = StockRecommendationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class TradeSignalCreateView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = TradeSignalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        trade_signals = TradeSignal.objects.all()
        serializer = TradeSignalSerializer(trade_signals, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class TradeListCreateAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = TradeingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        trades = Trade.objects.all()
        serializer = TradeingSerializer(trades, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)