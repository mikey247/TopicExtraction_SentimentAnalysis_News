from serpapi import GoogleSearch
import os

class SerpAPISearch:
    serp_api_key = ""

    def __init__(self, serp_api_key):
        print("SerpAPISearch initialized.", serp_api_key)
        self.serp_api_key = serp_api_key

    
    def search(self, search_query):

        params = {
            "engine": "google",
            "q": search_query,
            "location": "United Kingdom", 
            "hl": "en",
            "gl": "uk",
            "google_domain": "google.com",
            "num": "50",
            "safe": "active",
            "api_key": self.serp_api_key,
            "tbm": "nws"
        }

        search = GoogleSearch(params)
        results = search.get_dict()

        news_results = results.get("news_results", [])

        if not news_results:
            print("No news results found for the query.")
        
        return news_results
