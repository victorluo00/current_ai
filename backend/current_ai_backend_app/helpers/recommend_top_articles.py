from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import ast
from .data_cleaning import preprocess_df

def recommend_top_articles(df, user_preferences):
  # Create a TfidfVectorizer to vectorize the tags
  vectorizer = TfidfVectorizer()
  # Preprocess df for vectorization
  df = preprocess_df(df)
  # Vectorize the tags
  tag_vectors = vectorizer.fit_transform(df['tags'].apply(lambda x: ' '.join(ast.literal_eval(x))))
  print('user', user_preferences)
  # Vectorize the user preferences
  # user_vector = vectorizer.transform([' '.join(user_preferences)])

  user_vector = vectorizer.transform([' '.join(user_preferences)])

  # Calculate cosine similarity between user preferences and article tags
  similarity_scores = cosine_similarity(user_vector, tag_vectors)

  # Get indices of articles with highest similarity scores
  top_articles_indices = similarity_scores.argsort()[0][::-1][:5]

  # Get the actual articles based on the indices
  top_articles = df.iloc[top_articles_indices]
  return top_articles