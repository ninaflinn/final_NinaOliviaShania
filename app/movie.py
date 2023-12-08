import json

from dotenv import load_dotenv
import requests

from app.alpha import API_KEY

def get_genre_list():
    url = 'https://api.themoviedb.org/3/genre/movie/list'
    params = {
        'api_key': API_KEY,
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





