
from Utils import Utils
from controllers.LDATopicExtraction import LDATopicExtraction
from controllers.GoogleNewsSearch import GoogleNewsSearch
import os
import pandas as pd

utils = Utils()
lda = LDATopicExtraction()
googleNewsSearch = GoogleNewsSearch(os.getenv("API_KEY"),os.getenv("SEARCH_ENGINE_ID"))

data = pd.read_csv("datasets/news-websites_aux-data.csv")
news_websites = data['website']

# print news websites one per line
# for website in news_websites:
#     print(website+",")

class AlternativeNewsArticles:
    def __init__(self):
        print("AlternativeNewsArticles controller initialised")

    def get_alternative_news_articles(self, query):
        topics = lda.extract_topics(query)
        print("Topics are:", topics)
        search_term = utils.generate_perplexity_search_terms(topics)
        print("Search term is:", search_term)
        googleNewsSearch.set_query(search_term, 1)
        search_results = googleNewsSearch.get_search_results(100) 
        return search_results
    
    def get_alternative_news_articles_by_url(self, url):
        text = utils.get_text_from_url(url)
        topics = lda.extract_topics(text)
        print("Topics are:", topics)
        search_term = utils.generate_perplexity_search_terms(topics)
        print("Search term is:", search_term)
        googleNewsSearch.set_query(search_term, 1)
        search_results = googleNewsSearch.get_search_results(100)
        print("Search results are:", search_results)
        return search_results
