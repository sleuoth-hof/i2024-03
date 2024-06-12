import csv
from Feed.collectAllFeed import collect_feed


def existing_titles_list(csv_file_name):
    existing_titles = []
    try:
        with open(csv_file_name, 'r', encoding='utf-8', newline='') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)
            for row in csv_reader:
                if len(row) > 1:
                    existing_titles.append(row[1])
        return existing_titles
    except FileNotFoundError:
        pass
    return existing_titles


def append_news_to_csv(news_list, csv_file_name):
    existing_titles = existing_titles_list(csv_file_name)
    new_news = [news for news in news_list if news[1] not in existing_titles]

    with open(csv_file_name, 'a', encoding='utf-8', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        if csv_file.tell() == 0:
            csv_writer.writerow(["website_name", "title", "link", "formatted_date", "article_text"])
        for news in new_news:
            csv_writer.writerow([news[0], news[1], news[2], news[3],
                                 news[4]])


csv_file_pale = "newsDataBase.csv"
# news_feed = [["test.com", "test_title", "test_link", "test_date", "test_text"],
#              ["test2.com", "test2_title", "test2_link", "test2_date", "test2_text"],
#              ["test3.com", "test3_title", "test3_link", "test3_date", "test3_text"]]
news_feed = collect_feed()
print(news_feed)
append_news_to_csv(news_feed, csv_file_pale)
