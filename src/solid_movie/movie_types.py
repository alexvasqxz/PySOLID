import abc
import requests
from typing import Any

# S: One class responsible for getting the URL
class Path(abc.ABC):

    def __init__(self, url: str):
        self.url = url


class Requester(abc.ABC):

    @abc.abstractmethod
    def download(self, path: Path):
        raise Exception("I am an interface")


class RequesterURL(Requester):

    # S: One method responsible for getting the URL request
    # I: This interface only uses this method without making the 
    # parent (Requester) use it
    # D: This interface is a child of the Requester interface
    def download(self, path: Path):
        return (requests.get(path.url)).text


class AllData(abc.ABC):

    def __init__(self, movies: Any, links: Any, crew: Any, ratings: Any, votes: Any):
        self.movies = movies
        self.links = links
        self.crew = crew
        self.ratings = ratings
        self.votes = votes


class MovieData(abc.ABC):

    # S - A class for something that might be repeated and use only once
    def __init__(self, title: Any, year: Any, place: Any, star_cast: Any, rating: Any, vote: Any, link: Any, key: Any):
        self.title = title
        self.year = year
        self.place = place
        self.star_cast = star_cast
        self.rating = rating
        self.vote = vote
        self.link = link
        self.key = key
