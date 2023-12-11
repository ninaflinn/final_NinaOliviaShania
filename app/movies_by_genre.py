
import json
from pprint import pprint

from dotenv import load_dotenv
import requests

from plotly.express import line
from app.alpha import MOVIE_API_KEY
from app.email_service import send_email

import requests

def search_movies_by_genre(genre_id, start_year=None, end_year=None, lang=None):
    # TMDb API endpoint for discovering movies by genre
    url = f'https://api.themoviedb.org/3/discover/movie'

    # Parameters for the API request
    params = {
        'api_key': MOVIE_API_KEY,
        'with_genres': genre_id,
    }

    try:
        # Make the API request
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse the JSON response
        data = response.json()

        # Extract and return the list of movies
        movies = data.get('results', [])

        # FILTER BY YEAR WITHIN RANGE
        if start_year and end_year:
            movies = [movie for movie in movies if int(start_year) <= int(movie['release_date'][:4]) <= int(end_year)]

        # FILTER BY LANGUAGE:
        if lang:
            movies = [movie for movie in movies if movie['original_language'] == lang]

        return movies

    except requests.exceptions.RequestException as e:
        print(f"Error making TMDb API request: {e}")
        return None


if __name__ == "__main__":
    genre_id = '28'
    
    # Search for movies by genre
    movies = search_movies_by_genre(genre_id)
    
    # Display the results
    if movies:
        for movie in movies:
            print(f"{movie['title']} ({movie['release_date']})")
    else:
        print("No movies found.")