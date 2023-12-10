
import json
from pprint import pprint

from dotenv import load_dotenv
import requests

from plotly.express import line
from app.alpha import MOVIE_API_KEY
from app.email_service import send_email

def get_genre_list():
    # TMDb API endpoint for getting the list of movie genres
    url = 'https://api.themoviedb.org/3/genre/movie/list'

    # Parameters for the API request
    params = {
        'api_key': MOVIE_API_KEY,
    }

    try:
        # Make the API request
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse the JSON response
        data = response.json()

        # Extract and return the list of genres
        genres = data.get('genres', [])
        return genres

    except requests.exceptions.RequestException as e:
        print(f"Error making TMDb API request: {e}")
        return None

if __name__ == "__main__":
    genres = get_genre_list()
    if genres:
        for genre in genres:
            print(f"{genre['id']}: {genre['name']}")
    else:
        print("Failed to retrieve the list of genres.")