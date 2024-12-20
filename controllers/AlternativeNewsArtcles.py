
from Utils import Utils
from controllers.LDATopicExtraction import LDATopicExtraction
from controllers.GoogleNewsSearch import GoogleNewsSearch
from controllers.SentimentAnalysis import SentimentAnalysis
from controllers.SerpAPISearch import SerpAPISearch
import os
import pandas as pd

utils = Utils()
lda = LDATopicExtraction()
sentimentAnalysis = SentimentAnalysis()
API_KEY = os.getenv("API_KEY")
SEARCH_ENGINE_ID = os.getenv("SEARCH_ENGINE_ID")
SERP_API_KEY = os.getenv("SERP_API_KEY")
# print("API_KEY is", API_KEY)
# print("SEARCH_ENGINE_ID is", SEARCH_ENGINE_ID)

googleNewsSearch = GoogleNewsSearch(API_KEY, SEARCH_ENGINE_ID)

serpiAPISearch = SerpAPISearch(SERP_API_KEY)

data = pd.read_csv("datasets/news-websites_aux-data.csv")
news_websites = data['URL']

# print news websites one per line
# for website in news_websites:
#     print(website+",")

class AlternativeNewsArticles:
    def __init__(self):
        # print("AlternativeNewsArticles controller initialised")
        pass

    def get_alternative_news_articles(self, query, source):
        topics = lda.extract_topics(query)
        print("Topics are:", topics)
        search_term = utils.generate_perplexity_search_terms(topics)
        # search_term = "News like"+source+" on"+search_term
        print("Search term is:", search_term)
        # googleNewsSearch.set_query(search_term, 1)
        search_results = serpiAPISearch.search(search_term)
        return search_results
    
    def get_alternative_news_articles_by_url(self, url, source):
        text = utils.get_text_from_url(url)
        topics = lda.extract_topics(text)
        print("Topics are:", topics)
        search_term = utils.generate_perplexity_search_terms(topics)
        print("Search term is:", search_term)

        # googleNewsSearch.set_query(search_term, 1)
        # search_results = googleNewsSearch.get_search_results(80)
        # print("Search results are:", search_results)
        search_results = serpiAPISearch.search(search_term)
        return search_results
    
    def process_results(self, search_results):
        # print("Processing results", search_results)
        for result in search_results:
            # print("Result is:", result)
            sentimentAnalysis.classify_article(result)
            # result['sentiment'] = sentiment
  
