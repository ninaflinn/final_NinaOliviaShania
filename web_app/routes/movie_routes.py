from flask import Blueprint, request, render_template

from app.movies_by_genre import search_movies_by_genre
from app.movies_by_director import search_movies_by_director
from app.movies_by_actor import search_movies_by_actor

movie_routes = Blueprint("movie_routes", __name__)

@movie_routes.route("/movie/form", methods=["GET"])
def movie_form():
    print("MOVIE FORM...")
    return render_template("movie_form.html")

@movie_routes.route("/movie/genre/dashboard", methods=["GET", "POST"])
def movie_genre_dashboard():
    try:
        if request.method == "POST":
            genre_id = request.form.get("genre_id")
            start_year = request.form.get("start_year")
            end_year = request.form.get("end_year")
            lang = request.form.get("lang")

            print("Received Form Data:", genre_id, start_year, end_year, lang)

            movies = search_movies_by_genre(genre_id, start_year, end_year, lang)

            print("Movies Retrieved:", movies)
            if movies:
                return render_template("movie_genre_dashboard.html", movies=movies)
            else:
                print("error")
                error_message = "No movies found for the specified criteria."
                return render_template("movie_form.html", error_message=error_message)

        print("Direct Access to Movie Genre Dashboard")
        return render_template("movie_genre_dashboard.html", movies=None)

    except Exception as e:
        print(f"Error: {e}")

        error_message = "An error occurred. Please check your input and try again."
        return render_template("movie_form.html", movies=None, error_message=error_message)


@movie_routes.route("/movie/director/form", methods=["GET"])
def movie_director_form():
    print("MOVIE FORM...")
    return render_template("movie_director_form.html")

@movie_routes.route("/movie/director/dashboard", methods=["GET", "POST"])
def movie_director_dashboard():
    try:
        if request.method == "POST":
            director_name = request.form.get("director_name")

            print("Received Form Data:", director_name) 

            movies = search_movies_by_director(director_name)

            #for movie in movies:
            #    print(movie['title'])
            #breakpoint()

            print("Movies Retrieved:", movies)

            if movies:
                return render_template("movie_director_dashboard.html", movies=movies)
            else:
                #print("error")
                error_message = "No movies found for the specified director."
                return render_template("movie_director_form.html", error_message=error_message)

        print("Direct Access to Movie Director Dashboard")
        return render_template("movie_director_dashboard.html", movies=None)

    except Exception as e:
        print(f"Error: {e}")

        error_message = "An error occurred. Please check your input and try again."
        return render_template("movie_director_form.html", error_message=error_message)

@movie_routes.route("/movie/actor/form", methods=["GET"])
def movie_actor_form():
    print("MOVIE FORM...")
    return render_template("movie_actor_form.html")

@movie_routes.route("/movie/actor/dashboard", methods=["GET", "POST"])
def movie_actor_dashboard():
    try:
        if request.method == "POST":
            actor_name = request.form.get("actor_name")

            print("Received Form Data:", actor_name)

            movies = search_movies_by_actor(actor_name)

            print("Movies Retrieved:", movies)

            if movies:
                return render_template("movie_actor_dashboard.html", movies=movies)
            else:
                error_message = "No movies found for the specified actor or actress."
                return render_template("movie_actor_form.html", error_message=error_message)

        print("Direct Access to Movie Actor Dashboard")
        return render_template("movie_actor_dashboard.html", movies=None)

    except Exception as e:
        print(f"Error: {e}")

        error_message = "An error occurred. Please check your input and try again."
        return render_template("movie_actor_form.html", error_message=error_message)

@movie_routes.route("/api/movies.json")
def movies_api():
    print("MOVIES DATA (API)...")

    url_params = dict(request.args)
    print("URL PARAMS:", url_params)
    
    genre_id = url_params.get("genre_id")
    start_year = url_params.get("start_year")
    end_year = url_params.get("end_year")
    lang = url_params.get("lang")

    try:
        movies = search_movies_by_genre(genre_id, start_year, end_year, lang)

        if movies:
            data = [movie.to_dict() for movie in movies]
            return {"genre_id": genre_id, "data": data}
        else:
            return {"message": "No movies found for the specified criteria."}, 404

    except Exception as err:
        print('OOPS', err)
        return {"message": "Movie data retrieval error. Please try again."}, 500
