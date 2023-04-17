import newspaper
from newspaper import Article
import nltk
nltk.download('punkt')

def generate_keywords(df):
  # loop through each row of the dataframe
  keywords_col = []
  summary_col = []
  for index, row in df.iterrows():
      # initialize the article
      article = Article(row['url'])

      # download and parse the article
      try:
          # download and parse the article
          article.download()
          article.parse()

      except newspaper.ArticleException as e:
          # handle the exception by printing an error message and skipping to the next article
          print(f"Error downloading article: {e}")
          keywords_col.append([])
          summary_col.append([])
          continue


      # extract the keywords and add them to the dataframe
      article.nlp()
      keywords = article.keywords
      keywords_col.append(keywords)
      # df.at[index, 'keywords'] = keywords

      # extract the summary and add it to the dataframe
      summary = article.summary
      summary_col.append(summary)
      df.at[index, 'summary'] = summary
  df['tags'] = keywords_col
  return df
