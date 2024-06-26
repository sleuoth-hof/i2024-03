from FeedDatabase.getTitileList import get_title_list
from Feed.WebScraping.coindesk import get_coindesk_feed
from Feed.WebScraping.bbcNews import get_bbc_news_feed
from Feed.WebScraping.abcNews import get_abc_news_feed
from Feed.WebScraping.cointelegraph import get_cointelegraph_feed

DELETE_INFO_DAYS = 1


def collect_feed(csv_file_name):
    db_title_list = get_title_list(csv_file_name)
    all_feed = []
    all_feed += get_bbc_news_feed(db_title_list, 1)
    all_feed += get_coindesk_feed(db_title_list, 1)
    all_feed += get_abc_news_feed(db_title_list, 1)
#    all_feed += get_cointelegraph_feed(db_title_list, 1)
    return all_feed
