import pandas as pd

def all_articles_json_to_df(all_articles):
  articles_list = []
  for article in all_articles:
      article_dict = {
          'source_id': article['source']['id'],
          'source_name': article['source']['name'],
          'author': article['author'],
          'title': article['title'],
          'description': article['description'],
          'url': article['url'],
          'urlToImage': article['urlToImage'],
          'publishedAt': article['publishedAt'],
          'content': article['content']
      }
      articles_list.append(article_dict)

  # convert list of dictionaries to pandas DataFrame
  df = pd.DataFrame(articles_list)
  df.drop_duplicates(subset=['title'], inplace=True)
  return df

def top_articles_to_text(top_articles):
  print('top_articles', top_articles)
  summaries = ''
  article_counter = 0
  for i, row in top_articles.iterrows():
      summaries += '\n' + '\n' + str(article_counter+1) + '. '
      summaries += row['summary'] + ' '
      article_counter += 1
  return summaries
