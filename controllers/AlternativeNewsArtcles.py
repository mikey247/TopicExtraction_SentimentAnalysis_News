
from Utils import Utils
from controllers.LDATopicExtraction import LDATopicExtraction
from controllers.GoogleNewsSearch import GoogleNewsSearch
import os
import pandas as pd

utils = Utils()
lda = LDATopicExtraction()
API_KEY = os.getenv("API_KEY")
SEARCH_ENGINE_ID = os.getenv("SEARCH_ENGINE_ID")
# print("API_KEY is", API_KEY)
# print("SEARCH_ENGINE_ID is", SEARCH_ENGINE_ID)

googleNewsSearch = GoogleNewsSearch(API_KEY, SEARCH_ENGINE_ID)

data = pd.read_csv("datasets/news-websites_aux-data.csv")
news_websites = data['URL']

# print news websites one per line
# for website in news_websites:
#     print(website+",")

class AlternativeNewsArticles:
    def __init__(self):
        # print("AlternativeNewsArticles controller initialised")
        pass

    def get_alternative_news_articles(self, query):
        topics = lda.extract_topics(query)
        print("Topics are:", topics)
        search_term = utils.generate_perplexity_search_terms(topics)
        print("Search term is:", search_term)
        googleNewsSearch.set_query(search_term, 1)
        search_results = googleNewsSearch.get_search_results(80) 
        return search_results
    
    def get_alternative_news_articles_by_url(self, url):
        text = utils.get_text_from_url(url)
        topics = lda.extract_topics(text)
        print("Topics are:", topics)
        search_term = utils.generate_perplexity_search_terms(topics)
        print("Search term is:", search_term)
        googleNewsSearch.set_query(search_term, 1)
        search_results = googleNewsSearch.get_search_results(80)
        # print("Search results are:", search_results)
        return search_results
    
    def process_results(self, search_results):
        sources = news_websites.tolist()
        final = []
        # print("Search results are:", search_results)     
        for result in search_results['results']:
            for source in sources:
                print("Source is", source)
                print("Display link is", result['displayLink'])
                # final.append(result)
                   
