import feedparser
import requests
from bs4 import BeautifulSoup


def fetch_nyt_posts():
    rss_url = "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml"
    feed = feedparser.parse(rss_url)

    if feed.get("entries"):
        return feed.entries
    else:
        print("Failed to fetch NYT posts.")
        return None


def extract_full_text(post_link):
    response = requests.get(post_link)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        news_text = ""
        paragraphs = soup.find_all("p")
        for paragraph in paragraphs:
            news_text += paragraph.text + "\n"
        return news_text
    else:
        print("Failed to fetch post content:", response.status_code)
        return None


def take_text_from_link(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, features="html.parser")

    for script in soup(["script", "style"]):
        script.extract()  # rip it out

    url_text = soup.get_text()

    lines = (line.strip() for line in url_text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    url_text = '\n'.join(chunk for chunk in chunks if chunk)

    return url_text


nyt_posts = fetch_nyt_posts()
if nyt_posts:
    for post in nyt_posts:
        title = post.title
        link = post.link
        text = take_text_from_link(link)
        description = post.description

        print("Title:", title)
        print("Link:", link)
        print("Text:", text)
        print("Description:", description)

        full_text = extract_full_text(link)
        if full_text:
            print("Full Text:", full_text)

        print("\n")
else:
    print("Failed to fetch NYT posts.")
