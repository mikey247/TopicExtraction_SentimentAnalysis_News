
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from gensim import corpora, models, similarities
import numpy as np
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import nltk
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.metrics.pairwise import cosine_similarity
import requests

from controllers.GoogleNewsSearch import GoogleNewsSearch

from Utils import Utils

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

utils = Utils()


class LDATopicExtraction:
 
    def extract_topics(self, text):
        stop_words = set(stopwords.words('english'))
        sentences = sent_tokenize(text)

        processed_sentences = []
        for sentence in sentences:
            words = word_tokenize(sentence.lower())
            words = [word for word in words if word.isalnum() and word not in stop_words]
            processed_sentences.append(' '.join(words))

        # print("Processed Sentences --->>>",processed_sentences)

        # Preprocess all articles
        processed_articles = [utils.preprocess_text(article) for article in processed_sentences]

        # Create dictionary and corpus
        dictionary = corpora.Dictionary(processed_articles)
        corpus = [dictionary.doc2bow(text) for text in processed_articles]

        # Perform LDA
        lda_model = models.LdaModel(corpus=corpus, id2word=dictionary, num_topics=2, passes=10)

        # Extract topics as an array of words
        topics = []
        for idx, topic in lda_model.print_topics(5):
            topic_words = re.findall(r'"([^"]*)"', topic)
            topics.append(topic_words)

        # print("Topics as arrays of words:")
        # print(topics)

        final=[]

        for i, topic_words in enumerate(topics):
            for word in topic_words:
                final.append(word)

        # print("Bag of Words --->>>",final)
        return final

