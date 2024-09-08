from newsapi import NewsApiClient
import requests

# Init
newsapi = NewsApiClient(api_key='07c5923acae84eeca89d0bae0fdab650')

all_articles = newsapi.get_everything(
    q='action april chancellor lock minimum pay pension pledge rachel reeves shadow strike strikes triple unfunded union wage wages workers',
                                      from_param='2024-08-10',
                                      to='2024-09-05',
                                      language='en',
                                      sort_by='relevancy',
                                      )


print(all_articles)


# http://api.mediastack.com/v1/news
#     ? access_key = d1cd6bb3f339c1a9dbf1e612ce842bd3

# response = requests.get("http://api.mediastack.com/v1/news?access_key=d1cd6bb3f339c1a9dbf1e612ce842bd3&keywords=taxes taxation income welfare deficits federal")
# print(response.json())