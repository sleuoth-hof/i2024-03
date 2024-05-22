import finnhub
from models.newsModel import News
from datetime import datetime


def fetch_news():
    api_key = "cokf2gpr01qq4pkujt6gcokf2gpr01qq4pkujt70"  # set up env and store api  key in env 
    finnhub_client = finnhub.Client(api_key=api_key)
    news = finnhub_client.general_news('general', min_id=0)

    for item in news:
        News.objects.update_or_create(
            id=item['id'],
            defaults={
                'category': item['category'],
                'datetime': datetime.fromtimestamp(item['datetime']),
                'headline': item['headline'],
                'image': item['image'],
                'related': item['related'],
                'source': item['source'],
                'summary': item['summary'],
                'url': item['url'],
            }
        )
