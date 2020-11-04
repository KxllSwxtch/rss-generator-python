import feedparser

url = 'https://t.me/s/netflix'


def main():
    try:
        # url_to_parse = str(input('Enter the url to get the RSS: '))
        parsed_feed = feedparser.parse(url)
        entries = parsed_feed['entries']
        feed = parsed_feed['feed']
        print(feed['summary'])
    except:
        print("An error occured")


if __name__ == "__main__":
    main()
