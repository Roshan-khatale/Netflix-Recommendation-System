import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv("data/movies.csv")
cv = CountVectorizer()
mat = cv.fit_transform(df['genres'])
sim = cosine_similarity(mat)
print("Similarity matrix ready.")