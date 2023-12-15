
import json

from dotenv import load_dotenv
import requests

from app.alpha import MOVIE_API_KEY

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
        response = requests.get(url, params=params)
        response.raise_for_status()  

        data = response.json()

        movies = data.get('results', [])

        if start_year and end_year:
            movies = [movie for movie in movies if int(start_year) <= int(movie['release_date'][:4]) <= int(end_year)]

        if lang:
            movies = [movie for movie in movies if movie['original_language'] == lang]

        for movie in movies:
            if movie.get('poster_path'):
                movie['poster_url'] = f"https://image.tmdb.org/t/p/w500{movie['poster_path']}"
            else:
                movie['poster_url'] = None

        return movies

    except requests.exceptions.RequestException as e:
        print(f"Error making TMDb API request: {e}")
        return None



if __name__ == "__main__":
    genre_id = '28'
    
    movies = search_movies_by_genre(genre_id)
    print(movies[0].keys())
    if movies:
        for movie in movies:
            print(f"{movie['title']} ({movie['release_date']})")
    else:
        print("No movies found.")