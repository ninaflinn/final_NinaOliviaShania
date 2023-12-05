import json

from dotenv import load_dotenv
import requests

from app.alpha import API_KEY

def fetch_data():
    request_url = f"https://api.themoviedb.org/3/movie/550?api_key={API_KEY}"
    parsed_response = json.loads(response.text)
    print(type(parsed_response))
    print(parsed_response.keys())
    #pprint(parsed_response)

    data = parsed_response["data"]
    return data   

def fetch_movie():
    request = f"https://api.themoviedb.org/3/search/movie?query=Jack+Reacher&api_key={API_KEY}"
    parsed_response = json.loads(response.text)
    print(type(parsed_response))
    print(parsed_response.keys())
    #pprint(parsed_response)

    data = parsed_response["data"]
    return data



#a = "https://api.themoviedb.org/3/search/movie?query=Jack+Reacher&api_key=c195830a96938e95ca34e5e4e3e34126"
#b = requests.get(a)
#data = json.loads(b.text)
#print(data)

if __name__ == "__main__":
    data = fetch_data
    movie = fetch_movie
    print("hello")




