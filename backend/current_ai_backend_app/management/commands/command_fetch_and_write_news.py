from django.core.management.base import BaseCommand
from current_ai_backend_app.models import NewsArticle
from current_ai_backend_app.helpers.data_transformers import all_articles_json_to_df, top_articles_to_text
from current_ai_backend_app.helpers.news_gathering import gather_articles
from current_ai_backend_app.helpers.recommend_top_articles import recommend_top_articles
from current_ai_backend_app.helpers.generate_keywords import generate_keywords
import pandas as pd
from datetime import datetime
import math

class Command(BaseCommand):
    help = 'Fetches news articles, uses ML to generate keywords and summaries, and writes them to the database'
    def handle(self, *args, **options):
      # Gather the articles
      # all_articles = gather_articles()
      # df = all_articles_json_to_df(all_articles)
      #import news_articles.csv from ../data/news_articles.csv
      df = pd.read_csv('current_ai_backend_app/data/news_articles.csv')

      # Generate the keywords
      # df = generate_keywords(df)

      # Create db table
      for _, row in df.iterrows():
        try:
            published_at = datetime.strptime(str(row['publishedAt']), '%Y-%m-%dT%H:%M:%SZ')
        except ValueError:
            published_at = None


        article = NewsArticle(
          source_id=row['source_id'],
          source_name=row['source_name'],
          author=row['author'],
          title=row['title'],
          description=row['description'],
          url=row['url'],
          urlToImage=row['urlToImage'],
          publishedAt=published_at,
          content=row['content'],
          summary=row['summary'],
          tags=row['tags']
        )

        # Save the Article object to the database
        article.save()
