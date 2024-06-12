from Feed.WebScraping.coindesk import get_coindesk_feed
from Feed.WebScraping.bbcNews import get_bbc_news_feed
from Feed.WebScraping.abcNews import get_abc_news_feed


DELETE_INFO_DAYS = 1


def collect_feed():
    all_feed = []
    all_feed += get_bbc_news_feed(1)
    all_feed += get_coindesk_feed(1)
    all_feed += get_abc_news_feed(1)
    return all_feed
