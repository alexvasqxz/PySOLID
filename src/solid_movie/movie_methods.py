from solid_movie.movie_types import Path, Requester, MovieData
from bs4 import BeautifulSoup


class Downloader:

    @staticmethod
    # S - One method responsible for getting the BeautifulSoup response based on a request response
    # D - We use the Requester interface but are being passed the RequesterURL (child) from the main function
    def download_movies(path: Path, requester: Requester):
        return BeautifulSoup(requester.download(path), 'lxml')
    
    @staticmethod
    def dict_movie(movie: MovieData):
        return {"movie_title": movie.title,
                "year": movie.year,
                "place": movie.place,
                "star_cast": movie.star_cast,
                "rating": movie.rating,
                "vote": movie.vote,
                "link": movie.link,
                "preference_key": movie.key}
