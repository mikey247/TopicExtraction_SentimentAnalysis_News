# Building an application that takes in news articles (either via link or text), extracts topics, and suggests alternative news articles on the same topic is a great idea. Here's a high-level overview of how you can achieve this:

# Step 1: Setting Up the Environment
# Before diving into the code, make sure you have the necessary tools and libraries installed. You'll primarily need BERTopic, requests, and possibly BeautifulSoup for scraping text from links, as well as sentence-transformers for embeddings.


# pip install bertopic requests beautifulsoup4 sentence-transformers
# Step 2: Extracting Text from a URL
# If a user provides a link to a news article, you'll need to scrape the text content. Here's a simple way to extract the main content from a news article:


import requests
from bs4 import BeautifulSoup

def extract_text_from_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # This is a very basic way to extract text; real-world usage might need more customization.
    paragraphs = soup.find_all('p')
    article_text = ' '.join([para.get_text() for para in paragraphs])
    
    return article_text
# Step 3: Topic Extraction using BERTopic
# Once you have the text, you can use BERTopic to extract topics. Here’s how you can set up BERTopic and extract topics from the article:


from bertopic import BERTopic

def extract_topics(text):
    topic_model = BERTopic()
    topics, probabilities = topic_model.fit_transform([text])
    
    # Get the topic information
    topic_info = topic_model.get_topic_info()
    
    # Return the dominant topic
    dominant_topic = topic_model.get_topic(topics[0])
    
    return dominant_topic, topic_info
# Step 4: Finding Alternative Articles
# To find alternative articles on the same topic, you can use a search API like Bing Search, Google Custom Search, or scrape news websites directly. For simplicity, here's a mock-up of how you might structure such a function:

import requests

def find_alternative_articles(topic_keywords):
    query = " ".join([word for word, _ in topic_keywords])
    # Use an API or search engine to find relevant articles
    # Here is a placeholder for an API call (this requires an API key and setup):
    # response = requests.get("YOUR_NEWS_API_ENDPOINT", params={"q": query})
    
    # Simulating search results
    alternative_articles = [
        {"title": "Article 1 on similar topic", "url": "http://example.com/article1"},
        {"title": "Article 2 on similar topic", "url": "http://example.com/article2"},
    ]
    
    return alternative_articles
# Step 5: Integrating the Components
# Finally, integrate all these components into a single function or application that handles user input (text or URL), processes the text, extracts the topic, and then finds alternative articles.


def process_news_article(input_data):
    # Determine if the input is a URL or raw text
    if input_data.startswith("http"):
        text = extract_text_from_url(input_data)
    else:
        text = input_data
    
    # Extract topics
    dominant_topic, _ = extract_topics(text)
    
    # Find alternative articles based on the extracted topic
    alternative_articles = find_alternative_articles(dominant_topic)
    
    return {
        "extracted_topic": dominant_topic,
        "alternative_articles": alternative_articles
    }

# Example usage:
input_data = "https://example.com/news_article"  # or plain text
results = process_news_article(input_data)

print("Extracted Topic:", results["extracted_topic"])
print("Alternative Articles:")
for article in results["alternative_articles"]:
    print(f"{article['title']}: {article['url']}")

# Summary:
# Text Extraction: Extract the main content from a URL or use provided text.
# Topic Modeling: Use BERTopic to extract the main topics from the news article.
# Search for Alternatives: Use an external API or a custom search function to find alternative articles on the same topic.
# Integration: Combine these steps into a cohesive application flow.
# Additional Enhancements:
# User Interface: Consider building a simple web interface using Flask or Django where users can input URLs or text.
# Advanced Search: Implement more sophisticated search strategies, perhaps integrating with multiple news APIs to find the best matching articles.
# Cache Results: Use caching to store previously fetched and processed articles to reduce redundant API calls and speed up the application.
# This setup provides a solid foundation to build upon and should be flexible enough to expand as your project grows.