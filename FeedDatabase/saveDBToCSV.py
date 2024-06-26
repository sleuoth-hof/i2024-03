import csv
import time
from Feed.collectAllFeed import collect_feed
from getTitileList import get_title_list


def append_news_to_csv(news_list, csv_file_name):
    new_news = [news for news in news_list]

    with open(csv_file_name, 'a', encoding='utf-8', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        if csv_file.tell() == 0:
            csv_writer.writerow(["website_name", "title", "link", "formatted_date", "article_text"])
        for news in new_news:
            csv_writer.writerow([news[0], news[1], news[2], news[3],
                                 news[4]])


csv_file_name = "newsDataBase.csv"
news_feed = collect_feed(csv_file_name)
append_news_to_csv(news_feed, csv_file_name)
# while True:
#     news_feed = collect_feed()
#     append_news_to_csv(news_feed, csv_file_pale)
#     time.sleep(60)
