import requests
import re
import pandas as pd


class GoogleNewsSearch:
    def __init__(self, API_KEY, SEARCH_ENGINE_ID):
        self.query = None
        self.search_url = None
        self.search_results = None
        self.articles = None
        self.text = None
        self.API_KEY = API_KEY
        self.SEARCH_ENGINE_ID = SEARCH_ENGINE_ID

    def set_query(self, query):
        self.query = query
        # turn query into a proper url string
        query = query.replace(' ', '+')
        query = query.replace('"', '')
        self.search_url = "https://www.googleapis.com/customsearch/v1?key="+self.API_KEY+"&cx="+self.SEARCH_ENGINE_ID+"&q="+query
        print("URL IS NOW", self.search_url) 

    def get_search_results(self):
        response = requests.get(self.search_url)
        self.search_results = response.json()
        return self.search_results

    def get_articles(self):
        articles = []
        for item in self.search_results['items']:
            articles.append({
                'title': item['title'],
                'link': item['link']
            })
        return articles

    def get_text(self):
        text = ''
        for article in self.articles:
            response = requests.get(article['link'])
            text += response.text
        return text

    def get_processed_text(self):
        text = re.sub(r'<[^>]*>', '', self.text)
        text = re.sub(r'\s+', ' ', text)
        return text

    def get_dataframe(self):
        return pd.DataFrame(self.articles)