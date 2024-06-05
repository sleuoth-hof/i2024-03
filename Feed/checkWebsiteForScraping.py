from bs4 import BeautifulSoup
import requests

url = "https://edition.cnn.com/"

html_doc = requests.get(url)
soup = BeautifulSoup(html_doc.text, 'html.parser')
post = soup.find(class_="dcr-16c50tn")
print(post)
link = url + post.a["href"]
print("link: " + link)
article_html = requests.get(link)
article_soup = BeautifulSoup(article_html.text, 'html.parser')
print(article_soup)
