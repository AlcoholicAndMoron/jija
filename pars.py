import requests
from bs4 import BeautifulSoup

film_namestxt = []
film_genrestxt = []
for i in range(1, 6):
    url = f'https://ru.kinorium.com/collections/imdb/233/?order=sequence&page={i}&perpage=50&show_viewed=1'
    request = requests.get(url)
    request.encoding = 'utf-8'
    soup = BeautifulSoup(request.text, "lxml")
    film_names = soup.find_all(class_="movie-title__text filmList__item-title-link-popup link-info-movie-type-film")
    film_genres = soup.find_all(class_="filmList__extra-info")
    for j in film_names:
        film_namestxt.append(j.text.strip().replace("/xa0", " "))
    for l in film_genres:
        film_genrestxt.append(l.text.strip().split(",")[0])
kino = zip(film_namestxt, film_genrestxt)
with open("films.txt", "w") as sus:
    for k in kino:
        sus.write(k[0] + ":" + k[1] + '\n')