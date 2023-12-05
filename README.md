# final_NinaOliviaShania

# Setup

Create and activate a virtual environment:

```sh
conda create -n final-env python=3.10

conda activate final-env
```

Install packages:

```sh
pip install -r requirements.txt
```

Obtain an [API Key from The Movie Database](https://developer.themoviedb.org/docs)

Create a ".env" file and paste in the following contents:

```sh
# this is the ".env" file...

MOVIEDB_API_KEY="_________"
```

Run the movie app:
```sh
#python app/movie.py
python -m app.movie
```