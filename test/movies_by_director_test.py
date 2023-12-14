from app.movies_by_director import search_movies_by_director

def test_searching():
    result = search_movies_by_director("Sofia Coppola")
    assert 'release_date' in list(result[0].keys()) 
    #['adult', 'backdrop_path', 'genre_ids', 'id', 'original_language', 'original_title', 'overview', 'popularity', 'poster_path', 'release_date', 'title', 'video', 'vote_average', 'vote_count', 'poster_url']