# my-first-app

# Setup

Create and activate a virtual environment:

```sh
conda create -n my-first-env python=3.10

conda activate my-first-env
```


Install packages:

```sh
pip install -r requirements.txt
```

Obtain an [API Key from TheMovieDB](https://developer.themoviedb.org/docs).

Create a ".env" file and paste in the following contents:

```sh
# this is the ".env" file...
FLASK_APP="web_app"
MOVIE_API_KEY = "_______"
```



# Usage


Run the movie genre dashboard:
```sh
python -m app.movies_by_genre
```

Run the movie director dashboard:
```sh
python -m app.movies_by_director
```

Run the movie actor dashboard:
```sh
python -m app.movies_by_actor
```

### Web App

Run the web app (then view in the browser at http://localhost:5000/):

```sh
# Mac OS:
FLASK_APP=web_app flask run

# Windows OS:
# ... if `export` doesn't work for you, try `set` instead
# ... or set FLASK_APP variable via ".env" file
export FLASK_APP=web_app
flask run
```

# Testing

Run tests:

```sh
pytest
```
