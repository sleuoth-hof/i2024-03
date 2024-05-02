import feedparser
import requests
from bs4 import BeautifulSoup

rss_url = "https://feeds.bbci.co.uk/news/rss.xml"

feed = feedparser.parse(rss_url)


for entry in feed.entries:
    news_link = entry.link

    response = requests.get(news_link)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")

        news_title = soup.find("title").text

        news_text = ""
        paragraphs = soup.find_all("p")
        for paragraph in paragraphs:
            news_text += paragraph.text + "\n"

        print(">>> News title:", news_title)
        print(">>> News content:", news_text)

    else:
        print("Error:", response.status_code)
