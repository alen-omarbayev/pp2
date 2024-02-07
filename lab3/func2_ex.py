from func2 import movies
#1
def IMDB_score(movies):
    return [movie["imdb"] > 5.5 for movie in movies]

print(IMDB_score(movies))

#2
