from func2 import movies
#1
def IMDB_score(movies):
    return [movie["imdb"] > 5.5 for movie in movies]

print(IMDB_score(movies))

#2
def sublist_IMDB(movies):
    return movies["imdb"] > 5.5

filtered_movies= list(filter(sublist_IMDB, movies))
for movie in filtered_movies:
    print(movie)

#3
def get_categories(movies):
    for movie in movies:
        if movie["category"]==type_of_category:
            print(movie["name"])
  
type_of_category=str(input())
get_categories(movies)

#4
def average_score(movies):
    average=0
    for movie in movies:
        average+=movie["imdb"]
    result=average/len(movies)
    return result

print(average_score(movies))

#5
def category_average_score(movies):
    avrg=0
    for movie in movies:
        if movie["category"]==category_type:
            avrg+=movie["imdb"]
    return avrg/len(movies)

category_type=str(input())
print (category_average_score(movies))