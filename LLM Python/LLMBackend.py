import requests
import json
from datetime import datetime, timedelta


geturl = "http://127.0.0.1:8000/news/"


def get_time_range():
    today = datetime.now().date()
    five_days_ago = today - timedelta(days=5)
    return five_days_ago, today


def filter_news_by_datetime(news_list, start_date, end_date):
    filtered_news = []
    for item in news_list:
        news_datetime = datetime.fromtimestamp(item["datetime"])  
        news_date = news_datetime.date()
        if start_date <= news_date <= end_date:
            filtered_news.append(item)
    return filtered_news


response = requests.get(geturl)

if response.status_code == 200:
    response_data = response.json()
    summaries = []


    start_date, end_date = get_time_range()

    filtered_news = filter_news_by_datetime(response_data, start_date, end_date)

    for item in filtered_news:
        summary = item.get("summary")
        if summary:
            summaries.append(summary)

    print("Summaries:")
    for summary in summaries:
        print(summary)

   
    url = 'http://54.156.122.83:11434/api/generate'
    for summary in summaries:
        data = {
            "model": "stockLLM",
            "prompt": summary,
            "format": "json",
            "stream": False
        }

    
    
        response = requests.post(url, json=data)

        if response.status_code == 200:
            cleanresponse = response.json()['response'].strip()
            try:
                filterresponse = json.loads(cleanresponse)
                filterresponse = {k.lower(): v for k, v in filterresponse.items()}

              
                if isinstance(filterresponse, dict) and \
                   'stock' in filterresponse and \
                   'confidence' in filterresponse and \
                   'advice' in filterresponse:
                    print(filterresponse)

                   
                    posturl = "http://127.0.0.1:8000/stockllm/"
                    json_data = json.dumps({
                        "stock": filterresponse["stock"],
                        "confidence": filterresponse["confidence"],
                        "advice": filterresponse["advice"]
                    })

                   
                    post_response = requests.post(posturl, data=json_data, headers={"Content-Type": "application/json"})

                    if post_response.status_code == 201:
                        print("Stock recommendation successfully posted:", filterresponse)
                    else:
                        print("Failed to post stock recommendation. Status code:", post_response.status_code)
                        print(post_response.json())
                else:
                    print("Format is not correct:", filterresponse)
            except json.JSONDecodeError:
                print("Error in JSON:", cleanresponse)
        else:
            print("Error with status code:", response.status_code)
else:
    print("Error:", response.status_code)