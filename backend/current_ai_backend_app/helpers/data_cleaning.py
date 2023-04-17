import ast


def preprocess_df(df):
  # remove duplicate rows based on title and summary
  df.drop_duplicates(subset=['title'], inplace=True)
  df.drop_duplicates(subset=['summary'], inplace=True)

  # remove empty tags
  df['tags'].apply(lambda x: print('x', x))
  df = df[df['tags'].apply(lambda x: x[0] == '[' and len(ast.literal_eval(x)) > 0)]
  stop_words = ['the', 'and', 'a', 'an', 'in', 'of', 'to', 'is', 'for', 'with', 'that']

  # Filter out rows where the 'tags' column only contains stop words
  df = df[~df['tags'].apply(lambda x: all(tag in stop_words for tag in ast.literal_eval(x)))]
  return df

