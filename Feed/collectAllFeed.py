from Feed.WebScraping.coindesk import get_coindesk_feed
from Feed.WebScraping.bbcNews import get_bbc_news_feed


def collect_feed():
    all_feed = []
    all_feed += get_bbc_news_feed()
    all_feed += get_coindesk_feed()
    return all_feed
