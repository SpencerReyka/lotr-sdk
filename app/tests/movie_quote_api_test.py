import pytest
import requests
from app.client.movie_quote_api import MovieQuoteAPI

BASE_URL = "https://the-one-api.dev/v2"
API_KEY = "your_api_key"

MOCK_MOVIES = [
    {
        "_id": "5cd95395de30eff6ebccde56",
        "name": "The Lord of the Rings Series",
        "runtimeInMinutes": 558,
        "budgetInMillions": 281,
        "boxOfficeRevenueInMillions": 2917,
        "academyAwardNominations": 30,
        "academyAwardWins": 17,
        "rottenTomatoesScore": 94
    },
    {
        "_id": "5cd95395de30eff6ebccde57",
        "name": "The Hobbit Series",
        "runtimeInMinutes": 462,
        "budgetInMillions": 675,
        "boxOfficeRevenueInMillions": 2932,
        "academyAwardNominations": 7,
        "academyAwardWins": 1,
        "rottenTomatoesScore": 66.33333333
    }
]
MOCK_QUOTES = [
    {
        "_id": "5cd96e05de30eff6ebcce9b8",
        "dialog": "Sauron's wrath will be terrible, his retribution swift.",
        "movie": "5cd95395de30eff6ebccde5b",
        "character": "5cd99d4bde30eff6ebccfea0",
        "id": "5cd96e05de30eff6ebcce9b8"
    },
    {
        "_id": "5cd96e05de30eff6ebcce9b9",
        "dialog": "The battle for Helm's Deep is over. The battle for Middle-earth is about to begin.",
        "movie": "5cd95395de30eff6ebccde5b",
        "character": "5cd99d4bde30eff6ebccfea0",
        "id": "5cd96e05de30eff6ebcce9b9"
    },
    {
        "_id": "5cd96e05de30eff6ebcce9ba",
        "dialog": "All our hopes now lie with two little Hobbits...",
        "movie": "5cd95395de30eff6ebccde5b",
        "character": "5cd99d4bde30eff6ebccfea0",
        "id": "5cd96e05de30eff6ebcce9ba"
    },
    {
        "_id": "5cd96e05de30eff6ebcce9cb",
        "dialog": "...somewhere in the wilderness.",
        "movie": "5cd95395de30eff6ebccde5b",
        "character": "5cd99d4bde30eff6ebccfea0",
        "id": "5cd96e05de30eff6ebcce9cb"
    },
]

def test_get_movies(requests_mock):
    requests_mock.get(BASE_URL + "/movie", json= MOCK_MOVIES)
    movies = MovieQuoteAPI(API_KEY).get_movies()
    assert len(movies) == 2

def test_get_movie(requests_mock):
    requests_mock.get(BASE_URL + "/movie/5cd95395de30eff6ebccde56", json = MOCK_MOVIES[0])
    movie = MovieQuoteAPI(API_KEY).get_movie('5cd95395de30eff6ebccde56')
    assert movie is not None

def test_get_movie_quotes(requests_mock):
    requests_mock.get(BASE_URL + "/movie/5cd96e05de30eff6ebcce9cb/quote", json = MOCK_QUOTES)
    quotes = MovieQuoteAPI(API_KEY).get_movie_quotes('5cd96e05de30eff6ebcce9cb')
    assert len(quotes) == 4