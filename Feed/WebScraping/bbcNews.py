# get last 70 news from bcc.com

import feedparser
import requests
from bs4 import BeautifulSoup
from dateutil.parser import parse


def get_bbc_news_feed():
    rss_url = "https://feeds.bbci.co.uk/news/rss.xml"
    newses = feedparser.parse(rss_url)
    website_name = "bbc.com"

    feed = []

    for news in newses.entries:
        title = news.title
        print("title: " + title)

        link = news.link
        print("link: " + link)

        article_date = news.published
        article_date = parse(article_date)
        formatted_date = article_date.strftime("%Y-%m-%d %H:%M:%S")
        print("date: " + formatted_date)

        response = requests.get(link)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")

            news_text = ""
            paragraphs = soup.find_all("p")
            for paragraph in paragraphs:
                news_text += paragraph.text + ". "
            news_text.split()

            print("text: " + news_text)
            print("")

            feed.append([website_name, title, link, formatted_date, news_text])
        else:
            print("Error:", response.status_code)

    return feed


# print(get_bbc_news_feed())
