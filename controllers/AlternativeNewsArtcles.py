
from Utils import Utils
from controllers.LDATopicExtraction import LDATopicExtraction
from controllers.GoogleNewsSearch import GoogleNewsSearch
import os

utils = Utils()
lda = LDATopicExtraction()
googleNewsSearch = GoogleNewsSearch(os.getenv("API_KEY"),os.getenv("SEARCH_ENGINE_ID"))


class AlternativeNewsArticles:
    def __init__(self):
        print("AlternativeNewsArticles controller initialised")

    def get_alternative_news_articles(self, query):
        topics = lda.extract_topics(query)
        # print("Topics are:", topics)
        search_term = utils.generate_perplexity_search_terms(topics)
        googleNewsSearch.set_query(search_term, 1)
        search_results = googleNewsSearch.get_search_results(10)
        return search_results
    
    def get_alternative_news_articles_by_url(self, url):
        text = utils.get_text_from_url(url)
        topics = lda.extract_topics(text)
        search_term = utils.generate_perplexity_search_terms(topics)
        googleNewsSearch.set_query(search_term, 1)
        search_results = googleNewsSearch.get_search_results(10)
        return search_results
