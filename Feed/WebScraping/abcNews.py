import feedparser
import requests
from bs4 import BeautifulSoup
from dateutil.parser import parse


# abc news rss feed links - https://abcnews.go.com/Site/page/rss-feeds-3520115


rss_feed_links = ["https://abcnews.go.com/abcnews/topstories", "https://abcnews.go.com/abcnews/usheadlines",
                  "https://abcnews.go.com/abcnews/internationalheadlines",
                  "https://abcnews.go.com/abcnews/politicsheadlines", "https://abcnews.go.com/abcnews/moneyheadlines",
                  "https://abcnews.go.com/abcnews/technologyheadlines",
                  "https://abcnews.go.com/abcnews/healthheadlines",
                  "https://abcnews.go.com/abcnews/entertainmentheadlines"]


def get_abc_news_feed():
    rss_url = "https://abcnews.go.com/abcnews/topstories"
    newses = feedparser.parse(rss_url)
    website_name = "abcnews.com"

    feed = []
    for news in newses.entries:
        title = news.title

        link = news.link

        article_date = parse(news.published)
        formatted_date = article_date.strftime("%Y-%m-%d %H:%M:%S")

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
            print(">>> Error: ", link, response.status_code)

    return feed


print(get_abc_news_feed())
