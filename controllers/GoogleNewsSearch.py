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

    def set_query(self, query, start):
        # print("start is", start)
        self.query = query
        # turn query into a proper url string
        query = query.replace(' ', '+')
        query = query.replace('"', '')
        self.search_url = "https://www.googleapis.com/customsearch/v1?key="+self.API_KEY+"&cx="+self.SEARCH_ENGINE_ID+"&orTerms=news"+"&dateRestrict=m1"+"&start="+str(start)+"&q="+query
        # self.search_url = "https://www.googleapis.com/customsearch/v1?key="+self.API_KEY+"&cx="+self.SEARCH_ENGINE_ID+"&start="+str(start)+"&q="+query
        # print("URL IS NOW", self.search_url) 
        # print("Query is now", self.query)

    def get_search_results(self, limit):
        try:
            i = 0
            results = []
            while i <= limit:
                # Set the query with pagination or offset
                self.set_query(self.query, i)
                
                # Attempt to make the request
                response = requests.get(self.search_url)
                response.raise_for_status()  # Raise an exception for HTTP errors
                
                # Try to parse JSON response
                self.search_results = response.json()

                # print("Search results:", self.search_results)

                # Check if 'items' exists in the JSON response
                if 'items' not in self.search_results:
                    return {
                        "error": "Malformed response: 'items' key not found.",
                        "status_code": 500
                    }

                # Process items
                items = self.search_results['items']
                results.extend(items)

                # If the number of items returned is less than expected (pagination size),
                # we know there are no more results to fetch, so we can stop.
                if len(items) < 10:
                    break

                # Pagination: increase offset
                i += 10
            
            # Return only the results up to the limit, even if we fetched more
            return results

        # Catch specific exceptions and handle them
        except requests.exceptions.RequestException as e:
            # Handle request errors (connection issues, timeouts, etc.)
            return {"error": f"Request error: {str(e)}", "status_code": 502}

        except ValueError:
            # Handle JSON parsing errors
            return {"error": "Failed to parse JSON response.", "status_code": 500}

        except Exception as e:
            # Catch all other unexpected exceptions
            return {"error": f"An unexpected error occurred: {str(e)}", "status_code": 500}

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