import requests

class MovieQuoteAPI:
    def __init__(self, auth_token):
        self.base_url = "https://the-one-api.dev/v2"
        self.auth_token = auth_token

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
        endpoint = f"/movie"
        return self.__make_call(endpoint)

    def get_movie(self, id):
        endpoint = f"/movie/{id}"
        return self.__make_call(endpoint)

    def get_movie_quotes(self, id):
        endpoint = f"/movie/{id}/quote"
        return self.__make_call(endpoint)

    def get_quotes(self):
        endpoint = f"/quote"
        return self.__make_call(endpoint)

    def get_quote(self, id):
        endpoint = f"/quote/{id}"
        return self.__make_call(endpoint)
