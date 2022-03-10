def clean_genres(genres):
    return genres.lower().replace("|", " ")

# Example usage: clean_genres("Comedy|Romance")