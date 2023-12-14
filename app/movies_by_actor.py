
import json
from pprint import pprint

from dotenv import load_dotenv
import requests

from plotly.express import line
from app.alpha import MOVIE_API_KEY

import requests

def search_movies_by_actor(actor_name):
    # TMDb API endpoint for searching for a person (actor)
    person_search_url = 'https://api.themoviedb.org/3/search/person'

    # Parameters for the person search API request
    person_search_params = {
        'api_key': MOVIE_API_KEY,
        'query': actor_name,
    }

    try:
        # Make the person search API request
        person_search_response = requests.get(person_search_url, params=person_search_params)
        person_search_response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse the JSON response for the person search
        person_search_data = person_search_response.json()

        # Extract the person (actor) ID from the search results
        person_id = None
        if person_search_data['results']:
            person_id = person_search_data['results'][0]['id']

        if person_id is not None:
            # TMDb API endpoint for getting a person's (actor's) movie credits
            person_credits_url = f'https://api.themoviedb.org/3/person/{person_id}/movie_credits'

            # Parameters for the person credits API request
            person_credits_params = {
                'api_key': MOVIE_API_KEY,
            }

            # Make the person credits API request
            person_credits_response = requests.get(person_credits_url, params=person_credits_params)
            person_credits_response.raise_for_status()  # Raise an exception for HTTP errors

            # Parse the JSON response for the person credits
            person_credits_data = person_credits_response.json()

            # Extract and return the list of movies with this person in an acting role
            movies = person_credits_data.get('cast', [])

            # Create a set to keep track of unique movie ids
            unique_movie_ids = set()

            # Filter out duplicate movies based on their id and only include movies where the person had an acting role
            filtered_movies = []
            for movie in movies:
                if movie.get('id') and movie['id'] not in unique_movie_ids and movie.get('character'):
                    unique_movie_ids.add(movie['id'])

                    # Fetch poster URL for the movie
                    if movie.get('poster_path'):
                        movie['poster_url'] = f"https://image.tmdb.org/t/p/w500{movie['poster_path']}"
                    else:
                        movie['poster_url'] = None

                    filtered_movies.append(movie)

            return filtered_movies

    except requests.exceptions.RequestException as e:
        print(f"Error making TMDb API request: {e}")
        return None

if __name__ == "__main__":
    actor_name = 'Ryan Gosling'
    movies = search_movies_by_actor(actor_name)

    # Display the results
    if movies:
        for movie in movies:
            print(f"{movie['title']} ({movie['release_date']}) - Character: {movie['character']}")
    else:
        print(f"No movies found for actor/actress {actor_name}.")
