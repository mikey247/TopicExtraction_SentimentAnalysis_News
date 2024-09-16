import urllib.request  # the lib that handles the url stuff

class Util:
    def __init__(self):
        pass

    def read_article_from_url(self, url):
        for line in urllib.request.urlopen(url):
         print(line.decode('utf-8')) # Decoding the binary data to text.