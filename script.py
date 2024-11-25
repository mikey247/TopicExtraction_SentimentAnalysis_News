
# import pandas as pd

# sheet = pd.read_csv('./datasets/news-websites_aux-data.csv')

# # print(sheet.head())

# import re

from controllers.SentimentAnalysis import SentimentAnalysis

# # def extract_source(url):
# #     domain = re.search(r'https?://(?:www\.)?([^/]+)', url)
# #     if domain:
# #         domain = domain.group(1)
# #         # Remove common suffixes
# #         domain = re.sub(r'\.co\.uk|\.com|\.org|\.net', '', domain)
# #         print("Domain is", domain)  
# #         final = domain.split('.')[-1].capitalize()
# #         return final
# #     return None

# # news_bias = {
# #     "BBC": "left-center",
# #     "Sun": "right",
# #     "Mirror": "left-center",
# #     "Dailymail": "right",
# #     "Independent": "left-center",
# #     "Guardian": "left-center",
# #     "Telegraph": "right",
# #     "Express": "right",
# #     "Times": "right-center",
# #     "Liverpoolecho": "left-center",
# #     "Birminghammail": "left-center",
# #     "Evening Standard": "right-center",
# #     "Yahoo": "left-center"
# # }

# # def classify_article(url):
# #     # url = result.get('link')
# #     source = extract_source(url)

# #     print("Source is", source)
    
# #     # Check if source is in our news_bias dictionary
# #     if source in news_bias:
# #         return news_bias[source]
    
# #     # If not found, check if the source is mentioned in the snippet
# #     # snippet = result.get('snippet', '').lower()

# #     # for key in news_bias:
# #     #     if key.lower() in snippet:
# #     #         return news_bias[key]
    
# #     return "Unknown"

# # # url = "https://www.independent.co.uk/news/uk/politics/pub-gardens-smoking-ban-starmer-uk-b2604274.html"
# # url = "https://www.theguardian.com/society/commentisfree/article/2024/sep/08/the-pub-garden-smoking-ban-is-a-drag-on-our-freedoms"
# # print(classify_article(url))


# from urllib.parse import urlparse
# from fuzzywuzzy import process

# def extract_domain(url):
#     return urlparse(url).netloc.lower()

# def remove_common_suffixes(domain):
#     common_suffixes = ['.co.uk', '.com', '.org', '.net']
#     for suffix in common_suffixes:
#         if domain.endswith(suffix):
#             return domain[:-len(suffix)]
#     return domain

# def extract_source(url):
#     domain = extract_domain(url)
#     domain = remove_common_suffixes(domain)
#     return domain.split('.')[-1]

# def get_best_match(source, news_bias_keys):
#     return process.extractOne(source, news_bias_keys, score_cutoff=80)

# def classify_article(result, news_bias):
#     url = result.get('link')
#     source = extract_source(url)
    
#     # Try to find a close match in our news_bias dictionary
#     best_match = get_best_match(source, list(news_bias.keys()))
    
#     if best_match:
#         bias = news_bias[best_match[0]]
#         result['bias'] = bias
#         return bias
    
#     # If not found, check if the source is mentioned in the snippet
#     snippet = result.get('snippet', '').lower()
#     for key in news_bias:
#         if key.lower() in snippet:
#             return news_bias[key]
    
#     return "Unknown"

# # Example usage:
# news_bias = {
#     "BBC": "left-center",
#     "Sun": "right",
#     "Mirror": "left-center",
#     "Daily Mail": "right",
#     "Independent": "left-center",
#     "Guardian": "left-center",
#     "Telegraph": "right",
#     "Express": "right",
#     "Times": "right-center",
#     "Liverpool Echo": "left-center",
#     "Birmingham Live": "left-center",
#     "Evening Standard": "right-center",
#     "Yahoo": "left-center",
#     "Manchester Evening News": "left-center",
# }

# # Test the function
# urls = [
#     "https://www.theguardian.com/society/commentisfree/article/2024/sep/08/the-pub-garden-smoking-ban-is-a-drag-on-our-freedoms",
#     "https://www.bbc.co.uk/news/uk-politics-58787684",
#     "https://www.dailymail.co.uk/news/article-9958963/Smoking-ban-beer-gardens-WILL-law-Pubs-face-fines-allowing-tobacco-outside.html",
#     "https://www.standard.co.uk/news/london/man-arrested-bailed-acid-attack-school-west-london-b1186128.html",
#     "https://www.manchestereveningnews.co.uk/news/greater-manchester-news/enjoying-family-day-out-blackpool-30040713",
#     "https://edition.cnn.com/2024/10/06/politics/harris-biden-breaks/index.html"
# ]

sentimentAnalysis = SentimentAnalysis()
bias = sentimentAnalysis.get_source_bias("BBC")
print(bias) 
# bias=""
# # bias = sentimentAnalysis.classify_article({"link":"bbc.com"})
#    # Try to find a close match in our news_bias dictionary
# best_match = sentimentAnalysis.get_best_match("BBC", list(sentimentAnalysis.news_bias.keys()))
        
# if best_match:
#     bias = sentimentAnalysis.news_bias[best_match[0]]
#             # print("Source is", source, "Bias is", bias)

# print(bias)

# for url in urls:
#     result = {"link": url}
#     source = sentimentAnalysis.extract_source(url)
#     bias = sentimentAnalysis.classify_article(result)

#     print(result)
#     # print(f"URL: {url}")
#     # print(f"Extracted Source: {source}")
#     # print(f"Political Bias: {bias}")
#     # print()

# from serpapi import GoogleSearch

# params = {
#   "engine": "google",
#   "q": "UK government approaches smoking ban in outdoor hospitality venues",
#   "location": "United Kingdom", 
#   "hl": "en",
#   "gl": "uk",
#   "google_domain": "google.com",
#   "num": "50",
# #   "start": "10",
#   "safe": "active",
# }

# search = GoogleSearch(params)
# results = search.get_dict()
# organic_results = results["organic_results"]

# for result in organic_results:
#     print(result["title"])
#     print(result["link"])
#     print(result["snippet"])
#     print()