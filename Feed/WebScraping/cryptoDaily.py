import feedparser
import requests
from bs4 import BeautifulSoup
from dateutil.parser import parse
from datetime import datetime


def get_crypto_daily_feed(db_title_list, delete_info_days):
    rss_url = "https://cryptodaily.co.uk/"
    newses = feedparser.parse(rss_url)
    website_name = "cryptodaily.com"

    feed = []

    for news in newses.entries:
        title = news.title
        if title in db_title_list:
            break
        link = news.link

        article_date = news.published
        article_date = parse(article_date)
        formatted_date = article_date.strftime("%Y-%m-%d %H:%M:%S")
        date_obj = datetime.strptime(formatted_date, "%Y-%m-%d %H:%M:%S")
        current_time = datetime.utcnow()
        time_difference = current_time - date_obj
        if time_difference.days > delete_info_days:
            break

        response = requests.get(link)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")

            news_text = ""
            paragraphs = soup.find_all("p")
            for paragraph in paragraphs:
                news_text += paragraph.text + ". "
            news_text.split()

            feed.append([website_name, title, link, formatted_date, news_text])
        else:
            print(">>> bbcNews response Error:", response.status_code)

    return feed


# print(get_bbc_news_feed(1))
