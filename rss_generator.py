import feedparser

test_url = 'https://news.google.com/search?q=bussiness&hl=en-US&gl=US'


def main():
    d = feedparser.parse(test_url)
    dct = {}
    for key in d:
        d[key] = key
    print(dct)


if __name__ == '__main__':
    main()
