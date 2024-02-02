from bs4 import BeautifulSoup
import requests

url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url=url)

empire_web = response.text

soup = BeautifulSoup(empire_web, "html.parser")


hundred_movies = soup.find_all(name="h3", class_="title")
movie_name_list = []

for movie in hundred_movies:
    if movie.getText()[2] == ":" or movie.getText()[1] == ":":
        movie_name_list.append( movie.getText().split(": ")[1])
    else:    
        movie_name_list.append( movie.getText().split(") ")[1])

movie_name_list.reverse()
with open("moviefile.txt", "w", encoding="utf-8") as file:
    for indx, movie in enumerate(movie_name_list, 1):
        file.write(f"{indx}) {movie}\n")