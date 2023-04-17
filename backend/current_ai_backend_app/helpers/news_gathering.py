import os
from newsapi import NewsApiClient
from dotenv import load_dotenv

load_dotenv()

NEWS_API_KEY = os.getenv('NEWS_API_KEY')

def gather_articles():
  newsapi = NewsApiClient(api_key=NEWS_API_KEY)
  all_articles = []
  q_list = ['tech', 'business', 'politics', 'pop culture', 'election']
  for q_ele in q_list:
    articles_page = newsapi.get_everything(q=q_ele,
                                          language='en',
                                          from_param='2023-04-14',
                                          to='2023-04-15',
                                          sort_by='relevancy')
    all_articles += articles_page['articles']
  return all_articles



