from app.client.movie_quote_api import MovieQuoteAPI

class MovieQuoteSDK:
    def __init__(self, auth_token):
        self.movie_quote_api = MovieQuoteAPI(auth_token)

    def __make_call(self, endpoint):
        url = f"{self.base_url}{endpoint}"
        headers = {"Authorization": f"Bearer {self.auth_token   }"}
        response = requests.get(url, headers=headers)
        if response != None:
            print(response.json())
            return response.json()
        else:
            return response

    def get_movies(self):
        return self.movie_quote_api.get_movies()

    def get_movie(self, id):
        return self.movie_quote_api.get_movie(id)

    def get_movie_quotes(self, id):
        return self.movie_quote_api.get_movie_quotes(id)

    def get_quotes(self):
        return self.movie_quote_api.get_quotes()

    def get_quote(self, id):
        return self.movie_quote_api.get_quote(id)
