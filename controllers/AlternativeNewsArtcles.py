
from Utils import Utils
from controllers.LDATopicExtraction import LDATopicExtraction
from controllers.GoogleNewsSearch import GoogleNewsSearch


utils = Utils()
lda = LDATopicExtraction()
googleNewsSearch = GoogleNewsSearch("AIzaSyDtAsDFtdWtSw5FXM9VV1PBHvSzsIZ_vrc", "5000c0bd58ef54a2c")


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
