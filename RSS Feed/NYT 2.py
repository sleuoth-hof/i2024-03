from bs4 import BeautifulSoup
import requests

url = "https://www.nytimes.com/international/"

html_doc = requests.get(url)
# response - answer. make get request to take html document of url

soup = BeautifulSoup(html_doc.text, 'html.parser')

newses = soup.find_all(class_="story-wrapper")

# into news blocks
for news in newses:
    headline = news.find(class_="css-xdandi")
    title = headline.text.strip()
    print(title)
    link = news.a["href"]
    print(link)

    # article page
    article_html = requests.get(link)
    article_soup = BeautifulSoup(article_html.text, 'html.parser')
    print(article_soup)
    article_content = article_soup.find_all(class_="StoryBodyCompanionColumn")
    print(article_content)
    for storyBody in article_content:
        print(storyBody)
    # article_p = article_content.find_all('p')
    # article_text = ''
    # for text in article_p:
    #     article_text += text.text.strip()
    # article_text = article_content.text.strip()
    # strip() - delete the big spaces
    # print(article_text)

