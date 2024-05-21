import requests
import json
from models.newsModel  import  News
from models.newsEvaluation import NewsEvaluation

def evaluate_news():
    url = 'http://54.160.75.113:11434/api/generate'
    
    news_items = News.objects.all()
    
    for news_item in news_items:
        news = news_item.headline
        data = {
            "model": "stockLLM",
            "prompt": news,
            "format": "json",
            "stream": False
        }
        response = requests.post(url, json=data)
        
        if response.status_code == 200:
            try:
                result = response.json()
                stock_info = result['response'].strip()
                stock_info_dict = json.loads(stock_info)
                confidence = stock_info_dict.get('confidence')
                advice = stock_info_dict.get('advice')
                
                NewsEvaluation.objects.update_or_create(
                    news_name=news,
                    defaults={
                        'date': news_item.datetime.date(),  
                        'confidence': confidence,
                        'advice': advice,
                    }
                )
            except (KeyError, ValueError) as e:
                print("Error in JSON:", e)
        else:
            print("Error in response  status code", response.status_code)


evaluate_news()