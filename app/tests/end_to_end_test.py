import pytest
import requests
import os
from app.client.movie_quote_api import MovieQuoteAPI
from app.core.movie_quote_sdk import MovieQuoteSDK

BASE_URL = "https://the-one-api.dev/v2"
API_KEY_ENV_VAR_NAME = "sdk_lotr_token"

def movie_quote_setup():
    value = os.environ.get(API_KEY_ENV_VAR_NAME)
    if value is None:
        raise ValueError(f"Environment variable '{API_KEY_ENV_VAR_NAME}' not found.")

    return MovieQuoteSDK(value)

def test_get_movies():
    movie_quote_sdk = movie_quote_setup()
    movies = movie_quote_sdk.get_movies()
    assert len(movies) == 6

def test_get_movie():
    movie_quote_sdk = movie_quote_setup()
    movie = movie_quote_sdk.get_movie('5cd95395de30eff6ebccde56')
    assert movie is not None

def test_get_movie_quotes():
    movie_quote_sdk = movie_quote_setup()
    quotes = movie_quote_sdk.get_movie_quotes('5cd96e05de30eff6ebcce9cb')
    assert len(quotes) == 6

def test_get_quotes():
    movie_quote_sdk = movie_quote_setup()
    quotes = movie_quote_sdk.get_quotes()
    assert len(quotes) == 6

def test_get_quote():
    movie_quote_sdk = movie_quote_setup()
    quotes = movie_quote_sdk.get_movie_quotes('5cd96e05de30eff6ebcce7e9')
    assert len(quotes) == 6