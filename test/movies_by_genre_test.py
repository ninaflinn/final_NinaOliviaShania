from app.movies_by_genre import search_movies_by_genre

def test_searching():
    result = search_movies_by_genre(28)
    assert result[0]['title'] == "Freelance"