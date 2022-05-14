import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

data = pd.read_csv("data/movies.csv")
count = CountVectorizer()
matrix = count.fit_transform(data["genres"])
similarity = cosine_similarity(matrix)

print("Similarity matrix calculated.")