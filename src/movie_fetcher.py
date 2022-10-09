# Gustavo Alejandro Vasquez Acosta
# A00823326

import re
import csv

from solid_movie.movie_types import Path, RequesterURL, AllData, MovieData
from solid_movie.movie_methods import Downloader

# Please find all of my code changes in this file along with the files
# inside the solid_movie folder (movie_methods.py and movie_types.py)

# S -The Single Responsibility Principle
# I applied this principle on the Comments starting with Letter S, where I
# explain the reasons behind these changes, in summary, by creating multiple classes
# for each important piece of data an single methods for each action in order to lower 
# coupling

# I - The Interface Segregation Principle
# I applied this principle on the Comments starting with Letter I, in summary,
# by restricting each interface to a method it's going to use and no other 
# interfaces to use this method, I splitted some interfaces into smaller ones in order
# to reduce complexity

# D - Dependency Inversion Principle
# I applied this principle on the Comments starting with Letter D, in summary,
# this principle is apply when using the RequesterURL interface in here for calling
# the Downloader method, but in the movie_methods file using the Requester interface
# which is parent of RequesterURL, like the principle mentions, Never mention the name of 
# anything concrete and volatile

def main():

    path = Path("http://www.imdb.com/chart/top")
    requester = RequesterURL()
    soup = Downloader.download_movies(path, requester)

    data = AllData(soup.select('td.titleColumn'),
                   [a.attrs.get('href')
                    for a in soup.select('td.titleColumn a')],
                   [a.attrs.get('title')
                    for a in soup.select('td.titleColumn a')],
                   [b.attrs.get('data-value')
                    for b in soup.select('td.posterColumn span[name=ir]')],
                   [b.attrs.get('data-value') for b in soup.select('td.ratingColumn strong')])

    list = []

    for index in range(0, len(data.movies)):

        movie_string = data.movies[index].get_text()
        movie = (' '.join(movie_string.split()).replace('.', ''))

        tempMovie = MovieData(
            movie[len(str(index)) + 1:-7],
            re.search('\((.*?)\)', movie_string).group(1),
            movie[:len(str(index)) - (len(movie))],
            data.crew[index],
            data.ratings[index],
            data.votes[index],
            data.links[index],
            index % 4 + 1)

        list.append(Downloader.dict_movie(tempMovie))

    fields = ["preference_key", "movie_title", "star_cast",
              "rating", "year", "place", "vote", "link"]
    with open("movie_results.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        for movie in list:
            writer.writerow({**movie})


if __name__ == '__main__':
    main()
