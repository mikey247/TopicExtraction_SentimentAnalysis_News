import json
from urllib.parse import urlparse
import pandas as pd
from urllib.parse import urlparse
from fuzzywuzzy import process



class SentimentAnalysis:

    news_bias = None

    def __init__(self):
        data = pd.read_csv("datasets/news-websites_aux-data.csv")
        website = data['website']
        political_bias = data['political bias']

        self.news_bias = dict(zip(website, political_bias))

    def extract_domain(self, url):
        return urlparse(url).netloc.lower()

    def remove_common_suffixes(self, domain):
        common_suffixes = ['.co.uk', '.com', '.org', '.net']
        for suffix in common_suffixes:
            if domain.endswith(suffix):
                return domain[:-len(suffix)]
        return domain

    def extract_source(self, url):
        domain = self.extract_domain(url)
        domain = self.remove_common_suffixes(domain)
        return domain.split('.')[-1]

    def get_best_match(self, source, news_bias_keys):
        return process.extractOne(source, news_bias_keys, score_cutoff=80)

    def classify_article(self, result):
        url = result['link']
        # print("URL is", url)
        source = self.extract_source(url)
        
        # Try to find a close match in our news_bias dictionary
        best_match = self.get_best_match(source, list(self.news_bias.keys()))
        
        if best_match:
            bias = self.news_bias[best_match[0]]
            result['bias'] = bias
            return bias
        
        # If not found, check if the source is mentioned in the snippet
        # snippet = result.get('snippet', '').lower()
        # for key in self.news_bias:
        #     if key.lower() in snippet:
        #         return self.news_bias[key]
        
        return "Unknown"