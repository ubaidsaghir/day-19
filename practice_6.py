import pandas as pd

movies = {
    "Movie_ID": [1, 2, 3, 4, 5],
    "Title": ["Inception", "Avengers", "Interstellar", "Joker", "Titanic"],
    "Genre": ["Sci-Fi", "Action", "Sci-Fi", "Thriller", "Romance"],
    "Release_Year": [2010, 2012, 2014, 2019, 1997],
    "IMDB_Rating": [8.8, 8.1, 8.6, 8.5, 7.8],
    "Votes": [2000000, 1500000, 1400000, 1200000, 2200000]
}

df=pd.DataFrame(movies)
print(df)

experience_values = {
    1:45,
    2:46,
    3:47,
    4:48,
    5:49,
}

df["Experience"]=df["Movie_ID"].map(experience_values)
print(df)

