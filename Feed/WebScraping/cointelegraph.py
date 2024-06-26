from bs4 import BeautifulSoup
from datetime import datetime
import requests


def get_cointelegraph_feed(db_title_list, delete_info_days):
    url = "https://cointelegraph.com/"
    website_name = "cointelegraph.com"

    html_doc = requests.get(url)
    # response - answer. make get request to take html document of url

    soup = BeautifulSoup(html_doc.text, 'html.parser')
    print(soup.find_all("div"))
    newses = soup.find_all("div", class_="post-card")
    print(newses)
    feed = []

    # into news blocks
    for news in newses:
        headline = news.find("")
        title = headline.text.strip()
        if title in db_title_list:
            break
        link = url + news.a["href"]

        # article page
        article_html = requests.get(link)
        article_soup = BeautifulSoup(article_html.text, 'html.parser')

        time_element = article_soup.find('time')
        article_date = time_element['datetime']

        date_object = datetime.strptime(article_date, "%B %d, %Y at %I:%M %p UTC")
        formatted_date = date_object.strftime("%Y-%m-%d %H:%M:%S")
        date_obj = datetime.strptime(formatted_date, "%Y-%m-%d %H:%M:%S")
        current_time = datetime.utcnow()
        time_difference = current_time - date_obj
        if time_difference.days > delete_info_days:
            break

        article_text = ""
        paragraphs = soup.find_all("p")
        for paragraph in paragraphs:
            article_text += paragraph.text + ". "
        article_text.split()
        # strip() - delete the big spaces

        feed.append([website_name, title, link, formatted_date, article_text])
    return feed


print(get_cointelegraph_feed([], 1))
