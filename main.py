from bertopic import BERTopic
from bertopic.representation import KeyBERTInspired, OpenAI

from sklearn.datasets import fetch_20newsgroups
from sklearn.decomposition import PCA
from sentence_transformers import SentenceTransformer
from keybert import KeyBERT
from pandas import read_csv
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import nltk
nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

from single_text_processor import preprocess_text


abc_news = read_csv("./abcnews_sample.csv")
bbc_news = read_csv("./bbc_news.csv")

# documents = [
#     "I love programming in Python. Python is great for machine learning.",
#     "The capital of France is Paris.",
#     "Python has great libraries for data science.",
#     "Paris is a beautiful city with many historical sites.",
#     "Machine learning and data science are exciting fields.",
# ]
# documents = fetch_20newsgroups(subset='all', remove=('headers', 'footers', 'quotes'))['data']
# documents = abc_news["headline_text"].tolist()
documents = bbc_news["description"].tolist()

documents1 = ["""Unite calls for 1% wealth tax on super-rich to fund UK public sector pay rises The demand from Britains second biggest union will test truce with Labour at next month s TUC conferenceToby Helm Political EditorSat 24 Aug 2024 19.05 BST Share
              Britain s second biggest trade union is calling on the new Labour government to introduce an emergency 1% wealth tax on the assets of the super-rich to pay for 10% pay rises for public sector workers and fill more than 100,000 NHS vacancies. 
             The demand from Unite is in one of several motions to the Trades Union Congress, which meets in Brighton next month, that will expose tensions between 
             Keir Starmer s government and sections of the union movement. It comes as Rachel Reeves is preparing for her first budget as chancellor,
              on 30 October. Labour MPs and ministers believe that the TUC conference could mark the moment when an effective truce between many unions and Labour 
             –helping Starmer s general election campaign – may begin to break down as the prime minister and Reeves double down on their commitment to fiscal
              responsibility and stress the need for hard choices if the economy is to be restored to health. Other key trade unions are preparing to press for further 
             policy changes from Labour, including abandoning the two-child benefit cap, which Starmer has so far resisted, and the reversal of the recent decision to 
             end winter fuel payments for millions of pensioners, which has been causing a serious backlash among Labour backbenchers. While Reeves is understood to be considering increases in capital gains and inheritance taxes in the budget, Unites motion to the TUC conference goes much further, saying that, 
             with local authorities in financial peril, an urgently needed boost to public investment cannot wait for economic growth to materialise at an unspecified point in the future. 
             Unites plan is for a tax of 1% to be applied on the assets of those worth more than £4m, which it says would raise £25bn a year to fund investment in public services and avoid a return to austerity. Under the plan, someone with assets worth £6m would face a 1% tax on the £2m above the £4m threshold. 
             These assets would include property, shares and bank accounts but would not include mortgaged property.
              Unite points to research showing that the richest 50 families in the UK now have assets worth nearly £500bn.Sharon Graham, the general secretary of Unite, said: Unite s resolution to the TUC on the economy calls things by their real name. 
             The British economy is broken. Britain led the world s first industrial revolution. But due to decades of underinvestment in manufacturing and national infrastructure, we are now falling disastrously behind other countries in the new technological age and the transition to net zero. 
             We need serious investment in our crippled public services and in industry to ensure a prosperous future for Britain s workers and their communities. We won t get the money needed for that just by waiting for growth. 
             Unite was a big donor to the Labour party in 2019 but did not contribute to this year s election efforts, saying the election manifesto did not go far enough on protecting workers  rights and jobs in the oil and gas industry.The RMT transport union has also tabled a motion to the conference calling for a wealth tax to fund public investment, 
             and the abandonment of what it describes as unnecessarily restrictive and arbitrary fiscal rules which limit the government s ability to borrow. 
             A motion from the shop workers  union, Usdaw, calls for an end to the two-child benefit cap, and an amendment to the same motion from the PCS civil service union calls on the TUC to oppose cuts to the winter fuel allowance and demands appropriate taxation of corporations and the super-rich to fund the social security improvements identified in this motion.
              The TUC is also expected to press for pay restoration to make up for a decade of real-terms salary cuts for public sector workers. 
             Such demands will further add to the strains between Labour and its union backers after a series of pay deals between the Starmer-led government and striking workers in sectors ranging from healthcare to the railways.""",
            """The UK government has been urged to take action to prevent the spread of a new Covid variant that has been detected in South Africa. 
            The UK Health Security Agency said the variant, known as B.1.1.529, has a large number of mutations and has been designated a variant under investigation. 
            The World Health Organization has also been notified. The UKHSA said it was working with international partners to understand the potential impact of the variant. 
            It said the variant had been detected in South Africa and other countries, including Botswana, Hong Kong"""

            """The UK government has been urged to take action to prevent the spread of a new Covid variant that has been detected in South Africa.     
            The UK Health Security Agency said the variant, known as B.1.1.529, has a large number of mutations and has been designated a variant under investigation.
            The World Health Organization has also been notified. The UKHSA said it was working with international partners to understand the potential impact of the variant.
            It said the variant had been detected in South Africa and other countries, including Botswana, Hong Kong""",

            """Unite calls for 1% wealth tax on super-rich to fund UK public sector pay rises The demand from Britains second biggest union will test truce with Labour at next month s TUC conferenceToby Helm Political EditorSat 24 Aug 2024 19.05 BST Share
              Britain s second biggest trade union is calling on the new Labour government to introduce an emergency 1% wealth tax on the assets of the super-rich to pay for 10% pay rises for public sector workers and fill more than 100,000 NHS vacancies. 
             The demand from Unite is in one of several motions to the Trades Union Congress, which meets in Brighton next month, that will expose tensions between 
             Keir Starmer s government and sections of the union movement. It comes as Rachel Reeves is preparing for her first budget as chancellor,
              on 30 October. Labour MPs and ministers believe that the TUC conference could mark the moment when an effective truce between many unions and Labour 
             –helping Starmer s general election campaign – may begin to break down as the prime minister and Reeves double down on their commitment to fiscal
              responsibility and stress the need for hard choices if the economy is to be restored to health. Other key trade unions are preparing to press for further 
             policy changes from Labour, including abandoning the two-child benefit cap, which Starmer has so far resisted, and the reversal of the recent decision to 
             end winter fuel payments for millions of pensioners, which has been causing a serious backlash among Labour backbenchers. While Reeves is understood to be considering increases in capital gains and inheritance taxes in the budget, Unites motion to the TUC conference goes much further, saying that, 
             with local authorities in financial peril, an urgently needed boost to public investment cannot wait for economic growth to materialise at an unspecified point in the future. 
             Unites plan is for a tax of 1% to be applied on the assets of those worth more than £4m, which it says would raise £25bn a year to fund investment in public services and avoid a return to austerity. Under the plan, someone with assets worth £6m would face a 1% tax on the £2m above the £4m threshold. 
             These assets would include property, shares and bank accounts but would not include mortgaged property.
              Unite points to research showing that the richest 50 families in the UK now have assets worth nearly £500bn.Sharon Graham, the general secretary of Unite, said: Unite s resolution to the TUC on the economy calls things by their real name. 
             The British economy is broken. Britain led the world s first industrial revolution. But due to decades of underinvestment in manufacturing and national infrastructure, we are now falling disastrously behind other countries in the new technological age and the transition to net zero. 
             We need serious investment in our crippled public services and in industry to ensure a prosperous future for Britain s workers and their communities. We won t get the money needed for that just by waiting for growth. 
             Unite was a big donor to the Labour party in 2019 but did not contribute to this year s election efforts, saying the election manifesto did not go far enough on protecting workers  rights and jobs in the oil and gas industry.The RMT transport union has also tabled a motion to the conference calling for a wealth tax to fund public investment, 
             and the abandonment of what it describes as unnecessarily restrictive and arbitrary fiscal rules which limit the government s ability to borrow. 
             A motion from the shop workers  union, Usdaw, calls for an end to the two-child benefit cap, and an amendment to the same motion from the PCS civil service union calls on the TUC to oppose cuts to the winter fuel allowance and demands appropriate taxation of corporations and the super-rich to fund the social security improvements identified in this motion.
              The TUC is also expected to press for pay restoration to make up for a decade of real-terms salary cuts for public sector workers. 
             Such demands will further add to the strains between Labour and its union backers after a series of pay deals between the Starmer-led government and striking workers in sectors ranging from healthcare to the railways.""",
                
            """The UK government has been urged to take action to prevent the spread of a new Covid variant that has been detected in South Africa. 
            The UK Health Security Agency said the variant, known as B.1.1.529, has a large number of mutations and has been designated a variant under investigation. 
            The World Health Organization has also been notified. The UKHSA said it was working with international partners to understand the potential impact of the variant. 
            It said the variant had been detected in South Africa and other countries, including Botswana, Hong Kong"""

            """The UK government has been urged to take action to prevent the spread of a new Covid variant that has been detected in South Africa.     
            The UK Health Security Agency said the variant, known as B.1.1.529, has a large number of mutations and has been designated a variant under investigation.
            The World Health Organization has also been notified. The UKHSA said it was working with international partners to understand the potential impact of the variant.
            It said the variant had been detected in South Africa and other countries, including Botswana, Hong Kong"""
            """Unite calls for 1% wealth tax on super-rich to fund UK public sector pay rises The demand from Britains second biggest union will test truce with Labour at next month s TUC conferenceToby Helm Political EditorSat 24 Aug 2024 19.05 BST Share
              Britain s second biggest trade union is calling on the new Labour government to introduce an emergency 1% wealth tax on the assets of the super-rich to pay for 10% pay rises for public sector workers and fill more than 100,000 NHS vacancies. 
             The demand from Unite is in one of several motions to the Trades Union Congress, which meets in Brighton next month, that will expose tensions between 
             Keir Starmer s government and sections of the union movement. It comes as Rachel Reeves is preparing for her first budget as chancellor,
              on 30 October. Labour MPs and ministers believe that the TUC conference could mark the moment when an effective truce between many unions and Labour 
             –helping Starmer s general election campaign – may begin to break down as the prime minister and Reeves double down on their commitment to fiscal
              responsibility and stress the need for hard choices if the economy is to be restored to health. Other key trade unions are preparing to press for further 
             policy changes from Labour, including abandoning the two-child benefit cap, which Starmer has so far resisted, and the reversal of the recent decision to 
             end winter fuel payments for millions of pensioners, which has been causing a serious backlash among Labour backbenchers. While Reeves is understood to be considering increases in capital gains and inheritance taxes in the budget, Unites motion to the TUC conference goes much further, saying that, 
             with local authorities in financial peril, an urgently needed boost to public investment cannot wait for economic growth to materialise at an unspecified point in the future. 
             Unites plan is for a tax of 1% to be applied on the assets of those worth more than £4m, which it says would raise £25bn a year to fund investment in public services and avoid a return to austerity. Under the plan, someone with assets worth £6m would face a 1% tax on the £2m above the £4m threshold. 
             These assets would include property, shares and bank accounts but would not include mortgaged property.
              Unite points to research showing that the richest 50 families in the UK now have assets worth nearly £500bn.Sharon Graham, the general secretary of Unite, said: Unite s resolution to the TUC on the economy calls things by their real name. 
             The British economy is broken. Britain led the world s first industrial revolution. But due to decades of underinvestment in manufacturing and national infrastructure, we are now falling disastrously behind other countries in the new technological age and the transition to net zero. 
             We need serious investment in our crippled public services and in industry to ensure a prosperous future for Britain s workers and their communities. We won t get the money needed for that just by waiting for growth. 
             Unite was a big donor to the Labour party in 2019 but did not contribute to this year s election efforts, saying the election manifesto did not go far enough on protecting workers  rights and jobs in the oil and gas industry.The RMT transport union has also tabled a motion to the conference calling for a wealth tax to fund public investment, 
             and the abandonment of what it describes as unnecessarily restrictive and arbitrary fiscal rules which limit the government s ability to borrow. 
             A motion from the shop workers  union, Usdaw, calls for an end to the two-child benefit cap, and an amendment to the same motion from the PCS civil service union calls on the TUC to oppose cuts to the winter fuel allowance and demands appropriate taxation of corporations and the super-rich to fund the social security improvements identified in this motion.
              The TUC is also expected to press for pay restoration to make up for a decade of real-terms salary cuts for public sector workers. 
             Such demands will further add to the strains between Labour and its union backers after a series of pay deals between the Starmer-led government and striking workers in sectors ranging from healthcare to the railways.""",
                
            """The UK government has been urged to take action to prevent the spread of a new Covid variant that has been detected in South Africa. 
            The UK Health Security Agency said the variant, known as B.1.1.529, has a large number of mutations and has been designated a variant under investigation. 
            The World Health Organization has also been notified. The UKHSA said it was working with international partners to understand the potential impact of the variant. 
            It said the variant had been detected in South Africa and other countries, including Botswana, Hong Kong"""

            """The UK government has been urged to take action to prevent the spread of a new Covid variant that has been detected in South Africa.     
            The UK Health Security Agency said the variant, known as B.1.1.529, has a large number of mutations and has been designated a variant under investigation.
            The World Health Organization has also been notified. The UKHSA said it was working with international partners to understand the potential impact of the variant.
            It said the variant had been detected in South Africa and other countries, including Botswana, Hong Kong"""
            ]

document = """Unite calls for 1% wealth tax on super-rich to fund UK public sector pay rises The demand from Britains second biggest union will test truce with Labour at next month s TUC conferenceToby Helm Political EditorSat 24 Aug 2024 19.05 BST Share
              Britain s second biggest trade union is calling on the new Labour government to introduce an emergency 1% wealth tax on the assets of the super-rich to pay for 10% pay rises for public sector workers and fill more than 100,000 NHS vacancies. 
             The demand from Unite is in one of several motions to the Trades Union Congress, which meets in Brighton next month, that will expose tensions between 
             Keir Starmer s government and sections of the union movement. It comes as Rachel Reeves is preparing for her first budget as chancellor,
              on 30 October. Labour MPs and ministers believe that the TUC conference could mark the moment when an effective truce between many unions and Labour 
             –helping Starmer s general election campaign – may begin to break down as the prime minister and Reeves double down on their commitment to fiscal
              responsibility and stress the need for hard choices if the economy is to be restored to health. Other key trade unions are preparing to press for further 
             policy changes from Labour, including abandoning the two-child benefit cap, which Starmer has so far resisted, and the reversal of the recent decision to 
             end winter fuel payments for millions of pensioners, which has been causing a serious backlash among Labour backbenchers. While Reeves is understood to be considering increases in capital gains and inheritance taxes in the budget, Unites motion to the TUC conference goes much further, saying that, 
             with local authorities in financial peril, an urgently needed boost to public investment cannot wait for economic growth to materialise at an unspecified point in the future. 
             Unites plan is for a tax of 1% to be applied on the assets of those worth more than £4m, which it says would raise £25bn a year to fund investment in public services and avoid a return to austerity. Under the plan, someone with assets worth £6m would face a 1% tax on the £2m above the £4m threshold. 
             These assets would include property, shares and bank accounts but would not include mortgaged property.
              Unite points to research showing that the richest 50 families in the UK now have assets worth nearly £500bn.Sharon Graham, the general secretary of Unite, said: Unite s resolution to the TUC on the economy calls things by their real name. 
             The British economy is broken. Britain led the world s first industrial revolution. But due to decades of underinvestment in manufacturing and national infrastructure, we are now falling disastrously behind other countries in the new technological age and the transition to net zero. 
             We need serious investment in our crippled public services and in industry to ensure a prosperous future for Britain s workers and their communities. We won t get the money needed for that just by waiting for growth. 
             Unite was a big donor to the Labour party in 2019 but did not contribute to this year s election efforts, saying the election manifesto did not go far enough on protecting workers  rights and jobs in the oil and gas industry.The RMT transport union has also tabled a motion to the conference calling for a wealth tax to fund public investment, 
             and the abandonment of what it describes as unnecessarily restrictive and arbitrary fiscal rules which limit the government s ability to borrow. 
             A motion from the shop workers  union, Usdaw, calls for an end to the two-child benefit cap, and an amendment to the same motion from the PCS civil service union calls on the TUC to oppose cuts to the winter fuel allowance and demands appropriate taxation of corporations and the super-rich to fund the social security improvements identified in this motion.
              The TUC is also expected to press for pay restoration to make up for a decade of real-terms salary cuts for public sector workers. 
             Such demands will further add to the strains between Labour and its union backers after a series of pay deals between the Starmer-led government and striking workers in sectors ranging from healthcare to the railways."""

# Preprocessing
# stop_words = set(stopwords.words('english'))
# sentences = sent_tokenize(document)

# # # Tokenize and clean sentences
# processed_sentences = []
# for sentence in sentences:
#     words = word_tokenize(sentence.lower())
#     words = [word for word in words if word.isalnum() and word not in stop_words]
#     processed_sentences.append(' '.join(words))

# # Join back to form the document
# cleaned_document = '. '.join(processed_sentences)
# # # print(cleaned_document)
# sentences = document.split(".")

# # Initialize the embedding model
# embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
# # Fine-tune your topic representations
# representation_model = KeyBERTInspired()

# # Initialize BERTopic with a lower min_topic_size
# topic_model = BERTopic(embedding_model=embedding_model, verbose=True,representation_model=representation_model)

# # Fit the model using sentences as individual documents
# topics, probabilities = topic_model.fit_transform(documents)

# # Display the extracted topics
# print(topic_model.get_topic_info())

# dominant_topic = topic_model.get_topic(topics[0])
# print("Dominant Topic:", dominant_topic)

# Save the model
# topic_model.save("models/my_model")

# Load the model
loaded_model = BERTopic.load("models/my_model")


topics, probs = loaded_model.transform(document)
# result for document just transformed
print("Document topics:", topics)
# print("Document topics probabilities:", probs)

# print(loaded_model.get_topic_info())
topic_info = loaded_model.get_topic(topics[0])
print("Most relevant topic details:", topic_info)

# # Get detailed information about the most relevant topic
# if topics[0] != -1:
    # topic_info = loaded_model.get_topic(topics[0])
    # print("Most relevant topic details:", topic_info)
# else:
#     print("The document did not match any significant topics.")
#     topic_info = loaded_model.get_topic(-1)
#     print("The most relevant topic details:", topic_info)


# KEYBERT
# # Initialize KeyBERT model with a transformer model
# model = KeyBERT(model=SentenceTransformer('all-MiniLM-L6-v2'))
# # Extract keywords
# keywords = model.extract_keywords(document, keyphrase_ngram_range=(1, 2), stop_words='english', top_n=5)
# print("Extracted Keywords/Topics:", keywords)


# GENISM
# from gensim import corpora
# from gensim.models import LdaModel

# # Sample document
# texts = [cleaned_document.split()]

# # Create a dictionary and corpus
# dictionary = corpora.Dictionary(texts)
# corpus = [dictionary.doc2bow(text) for text in texts]

# # Apply LDA model
# lda = LdaModel(corpus, num_topics=1, id2word=dictionary, passes=10)
# topics = lda.print_topics(num_words=5)

# print("Extracted Topics:", topics)