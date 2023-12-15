
import json

from dotenv import load_dotenv
import requests

from app.alpha import MOVIE_API_KEY

import requests

def search_movies_by_director(director_name):
    # TMDb API endpoint for searching for a person (director)
    person_search_url = 'https://api.themoviedb.org/3/search/person'

    # Parameters for the person search API request
    person_search_params = {
        'api_key': MOVIE_API_KEY,
        'query': director_name,
    }

    try:
        person_search_response = requests.get(person_search_url, params=person_search_params)
        person_search_response.raise_for_status()  # Raise an exception for HTTP errors

        person_search_data = person_search_response.json()

        person_id = None
        if person_search_data['results']:
            person_id = person_search_data['results'][0]['id']

        if person_id is not None:
            person_credits_url = f'https://api.themoviedb.org/3/person/{person_id}/movie_credits'

            # Parameters for the person credits API request
            person_credits_params = {
                'api_key': MOVIE_API_KEY,
            }

            person_credits_response = requests.get(person_credits_url, params=person_credits_params)
            person_credits_response.raise_for_status()  # Raise an exception for HTTP errors

            person_credits_data = person_credits_response.json()

            movies = person_credits_data.get('crew', [])

            unique_movie_ids = set()

            filtered_movies = []
            for movie in movies:
                if movie.get('id') and movie['id'] not in unique_movie_ids:
                    unique_movie_ids.add(movie['id'])

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
    director_name = 'Sofia Coppola'
    movies = search_movies_by_director(director_name)

    if movies:
        for movie in movies:
            print(f"{movie['title']} ({movie['release_date']})")
    else:
        print(f"No movies found for director {director_name}.")
