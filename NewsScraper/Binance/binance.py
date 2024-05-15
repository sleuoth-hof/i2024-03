import requests
from bs4 import BeautifulSoup
import json
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def fetch_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.content
    except requests.RequestException as e:
        logging.error(f"Error fetching {url}: {e}")
        return None

def parse_binance_news(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    
    articles = []
    news_section = soup.find('div', class_='css-1m3isg3')
    if not news_section:
        logging.error("Could not find the news section in the HTML content.")
        return articles

    news_items = news_section.find_all('a', class_='css-1ej4hfo')
    for item in news_items:
        title = item.get_text().strip()
        link = item['href']
        if not link.startswith('http'):
            link = 'https://www.binance.com' + link

        articles.append({
            'title': title,
            'link': link
        })

    return articles

def save_to_json(data, filename='binance_news.json'):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def main():
    url = 'https://www.binance.com/en/news'
    html_content = fetch_html(url)
    
    if html_content:
        articles = parse_binance_news(html_content)
        if articles:
            save_to_json(articles)
            logging.info(f"Saved {len(articles)} articles to binance_news.json")
        else:
            logging.info("No articles found.")
    else:
        logging.error("Failed to retrieve the HTML content.")

if __name__ == "__main__":
    main()
