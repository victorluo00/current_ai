from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd
from current_ai_backend_app.models import NewsArticle
from current_ai_backend_app.helpers.data_transformers import all_articles_json_to_df, top_articles_to_text
from current_ai_backend_app.helpers.news_gathering import gather_articles
from current_ai_backend_app.helpers.recommend_top_articles import recommend_top_articles
from current_ai_backend_app.helpers.generate_keywords import generate_keywords


def load_data(request):
  queryset = NewsArticle.objects.all()
  article_list = list(queryset.values())
  df = pd.DataFrame(article_list)

  data = df.to_dict(orient='records')
  return JsonResponse({'data': data})

def recommend_top_articles_view(request, topics):
  # Gather the articles by calling load_data
  queryset = NewsArticle.objects.all()
  article_list = list(queryset.values())
  df = pd.DataFrame(article_list)
  print('topics', topics)
  # Recommend the top articles
  topics = topics.split(',')
  top_articles = recommend_top_articles(df, topics)
  print('top_articles', top_articles)
  # Convert the top articles to text
  summaries = top_articles_to_text(top_articles)
  print('summaries', summaries)
  return JsonResponse({'summaries': summaries})