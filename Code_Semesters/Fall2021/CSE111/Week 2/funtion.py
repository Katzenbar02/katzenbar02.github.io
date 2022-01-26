
def get_unsername():
    username = input("Please input your name: ")
    return username

def get_favorite_movies(username): #username equals my name :)

    while (True):
        favorite_movies = []
        movie_string = input("Please enter a coma-seperated listof your favorite movies: ")
        movie_list = movie_string.split(", ")
        print(movie_string)
        print(movie_list)
    
name = get_unsername()

get_favorite_movies(name)
print(name)