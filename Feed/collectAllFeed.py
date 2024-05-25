from Feed.WebScraping.coindesk import get_coindesk_feed


def collect_feed():
    all_feed = []
    all_feed += get_coindesk_feed()
    return all_feed
