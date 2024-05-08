# get last 6 news from coindesk.com

from bs4 import BeautifulSoup
import requests


def getCoindeskFeed():
    url = "https://www.coindesk.com/"

    html_doc = requests.get(url)
    # response - answer. make get request to take html document of url

    soup = BeautifulSoup(html_doc.text, 'html.parser')

    newses = soup.find_all(class_="static-cardstyles__StaticCardWrapper-sc-1kiw3u-0 iiwocm")

    feed = []

    # into news blocks
    for news in newses:
        headline = news.find(class_="card-titlestyles__CardTitleWrapper-sc-1ptmy9y-0 junCw card-title-link")
        title = headline.text.strip()
        print("title : " + title)
        link = url + news.a["href"]
        print("link: " + link)

        # article page
        article_html = requests.get(link)
        article_soup = BeautifulSoup(article_html.text, 'html.parser')
        article_content = article_soup.find(class_="contentstyle__StyledWrapper-sc-g5cdrh-0 gkcZwU composer-content")
        article_text = article_content.text.strip()
        # strip() - delete the big spaces
        print("text: " + article_text + '\n')
        feed += [title, link, article_text]
    return feed


# print(getCoindeskFeed())
