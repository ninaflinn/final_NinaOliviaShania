import json

from dotenv import load_dotenv
import requests

from app.alpha import API_KEY

def get_genre_list():
    # TMDb API endpoint for getting the list of movie genres
    url = 'https://api.themoviedb.org/3/genre/movie/list'

    # Parameters for the API request
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



def fetch_data():
    request_url = f"https://api.themoviedb.org/3/movie/550?api_key={API_KEY}"
    response = requests.get(request_url)
    parsed_response = json.loads(response.text)
    print(type(parsed_response))
    print(parsed_response.keys())
    #pprint(parsed_response)

    #data = parsed_response["genres"]
    return data   

if __name__ == "__main__":
    data = get_genre_list()
    print(data)





