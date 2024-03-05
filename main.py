from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
movie_site= response.text
soup = BeautifulSoup(movie_site, "html.parser")

article_tag = soup.find_all(name="h3", class_="title")
movie=[movie.getText() for movie in article_tag]
movie=movie[::-1]
#print(movie)

with open("movies.txt", mode="w") as file:
    for i in movie:
        file.write(f"{i}\n")