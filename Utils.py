import urllib.request  # the lib that handles the url stuff
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import requests

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import WordNetLemmatizer

import nltk
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.metrics.pairwise import cosine_similarity
import requests

from controllers.GoogleNewsSearch import GoogleNewsSearch

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
import os


class Utils:
    PERPLEXITY_API_KEY = os.getenv("PERPLEXITY_API_KEY")
    PERPLEXITY_API_URL = "https://api.perplexity.ai/chat/completions"

    def __init__(self):
        pass

    def preprocess_text(self, text):
        # Tokenize and lowercase
        tokens = word_tokenize(text.lower())
        
        # Remove stopwords and non-alphabetic tokens
        stop_words = set(stopwords.words('english'))
        tokens = [token for token in tokens if token.isalpha() and token not in stop_words]
        
        # Lemmatize
        lemmatizer = WordNetLemmatizer()
        tokens = [lemmatizer.lemmatize(token) for token in tokens]
        
        return tokens

    def get_text_from_url(self, url):
        # Set up Chrome WebDriver with headless option
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        
        try:
            # Fetch the URL using the browser simulation
            driver.get(url)
            
            # Get the page source and extract the text with BeautifulSoup
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            text = soup.get_text(separator=' ', strip=True)
            return text
        except Exception as e:
            return f"An error occurred: {e}"
        finally:
            driver.quit()
    

    def generate_perplexity_search_terms(self, topics):
        search_term = ""
        headers = {
            "Authorization": f"Bearer {self.PERPLEXITY_API_KEY}",
            "Content-Type": "application/json"
        }

        # print("Topics---:", topics)

        # Join topic words into a comma-separated string
        comma_separated_topics = ", ".join(topics)
        
        prompt = f"Given these topic words: {comma_separated_topics}. In 5 words or less and ONE SENTENCE, Generate a concise, relevant search term or phrase that captures the essence of this topic. The search term should be suitable for finding articles related to this topic online. Do not add unnecessary text as it may corrupt search results"
        
        data = {
            "model": "mistral-7b-instruct", 
            "messages": [
                {"role": "system", "content": "You are a helpful, concise assistant that generates a CONCISE and relevant search term based on given topic words, you does not add unnecessary text and bracketed information as it may corrupt search results. Provide ONE sentence search term that captures the essence of the topic. The sentence must be headline worthy, emphasizing the most important aspects of the topic and avoiding added text that skew results, this is very important, do not mention a news or media company or term just the topic of interest remove all additives!!!!."},
                {"role": "user", "content": prompt}
            ]
        }
        
        response = requests.post(self.PERPLEXITY_API_URL, json=data, headers=headers)
        if response.status_code == 200:
            search_term = response.json()['choices'][0]['message']['content'].strip()
            search_term = search_term
        else:
            print(f"Error: {response.status_code}, {response.text}")
            search_term = "Error generating search term" 

        sources = ["BBC", "Sun","Mirror", "Daily Mail", "Independent","Guardian","Manchester Evening News", "Sky News", "Metro", "Telegraph", "Daily Express", "Times", "Liverpool Echo", "Birmingham Live", "Evening Standard",]
        jp = " ".join(sources)
        return search_term

# Example usage
# url = "https://www.independent.co.uk/news/uk/politics/pub-gardens-smoking-ban-starmer-uk-b2604274.html"
# url = "https://www.independent.co.uk/news/uk/politics/pub-gardens-smoking-ban-starmer-uk-b2604274.html"
# utils = Utils()
# text_content = utils.get_text_from_url(url)
# print(text_content)












# from bs4 import BeautifulSoup
# import json
# import numpy as np
# import requests
# from requests.models import MissingSchema
# import spacy
# import trafilatura

# def beautifulsoup_extract_text_fallback(response_content):
    
#     '''
#     This is a fallback function, so that we can always return a value for text content.
#     Even for when both Trafilatura and BeautifulSoup are unable to extract the text from a 
#     single URL.
#     '''
    
#     # Create the beautifulsoup object:
#     soup = BeautifulSoup(response_content, 'html.parser')
    
#     # Finding the text:
#     text = soup.find_all(text=True)
    
#     # Remove unwanted tag elements:
#     cleaned_text = ''
#     blacklist = [
#         '[document]',
#         'noscript',
#         'header',
#         'html',
#         'meta',
#         'head', 
#         'input',
#         'script',
#         'style',]

#     # Then we will loop over every item in the extract text and make sure that the beautifulsoup4 tag
#     # is NOT in the blacklist
#     for item in text:
#         if item.parent.name not in blacklist:
#             cleaned_text += '{} '.format(item)
            
#     # Remove any tab separation and strip the text:
#     cleaned_text = cleaned_text.replace('\t', '')
#     return cleaned_text.strip()
    

# def extract_text_from_single_web_page(url):
    
#     downloaded_url = trafilatura.fetch_url(url)
#     try:
#         a = trafilatura.extract(downloaded_url, output_format="json", with_metadata=True, include_comments = False,
#                             # date_extraction_params={'extensive_search': True, 'original_date': True}
#         )
#     except AttributeError:
#         a = trafilatura.extract(downloaded_url, output_format="json", with_metadata=True,
#                             # date_extraction_params={'extensive_search': True, 'original_date': True}
#         )
#     if a:
#         json_output = json.loads(a)
#         return json_output['text']
#     else:
#         try:
#             resp = requests.get(url)
#             # We will only extract the text from successful requests:
#             if resp.status_code == 200:
#                 return beautifulsoup_extract_text_fallback(resp.content)
#             else:
#                 # This line will handle for any failures in both the Trafilature and BeautifulSoup4 functions:
#                 return np.nan
#         # Handling for any URLs that don't have the correct protocol
#         except MissingSchema:
#             return np.nan
# single_url = 'https://www.cato.org/regulation/summer-2010/economic-losers-smoking-bans'
# text = extract_text_from_single_web_page(url=single_url)
# print(text)



