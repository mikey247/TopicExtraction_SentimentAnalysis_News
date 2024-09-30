import json
from urllib.parse import urlparse
import pandas as pd

data = pd.read_csv("datasets/news-websites_aux-data.csv")
news_websites = data['URL']

class SentimentAnalysis:
    # Load source-sentiment dataset
    with open('source_sentiment.json', 'r') as file:
        source_sentiment_map = json.load(file)

    def extract_source_from_url(article_url):
        # Extract domain name from the article URL
        domain = urlparse(article_url).netloc
        return domain

    def get_sentiment_label(source):
        # Match source with sentiment label from dataset
        pass

    # # Example usage
    # article_url = "https://example.com/article"
    # source = extract_source_from_url(article_url)
    # sentiment_label = get_sentiment_label(source)

    # print(f"The sentiment label for {source} is {sentiment_label}")
