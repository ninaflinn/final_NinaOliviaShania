from app.movies_by_director import search_movies_by_director

def test_searching():
    result = search_movies_by_director("Sofia Coppola")
    assert result[0]['title'] == "New York Stories"