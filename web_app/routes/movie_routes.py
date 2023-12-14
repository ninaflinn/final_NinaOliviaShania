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
            # Get form data
            genre_id = request.form.get("genre_id")
            start_year = request.form.get("start_year")
            end_year = request.form.get("end_year")
            lang = request.form.get("lang")

            print("Received Form Data:", genre_id, start_year, end_year, lang)  # Check form data

            # Call function to get movies based on user criteria
            movies = search_movies_by_genre(genre_id, start_year, end_year, lang)

            print("Movies Retrieved:", movies)  # Check movies retrieved

            if movies:
                # Display movies if found
                return render_template("movie_genre_dashboard.html", movies=movies)
            else:
                # Handle case when no movies are found
                print("error")
                error_message = "No movies found for the specified criteria."
                return render_template("movie_genre_dashboard.html", error_message=error_message)

        # Direct access to the movie dashboard without form submission
        print("Direct Access to Movie Genre Dashboard")
        return render_template("movie_genre_dashboard.html", movies=None)

    except Exception as e:
        # Log the error for debugging purposes
        print(f"Error: {e}")

        # Render the form template with an error message
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
            # Get form data
            director_name = request.form.get("director_name")

            print("Received Form Data:", director_name)  # Check form data

            # Call function to get movies based on user criteria
            movies = search_movies_by_director(director_name)

            print("Movies Retrieved:", movies)  # Check movies retrieved

            if movies:
                # Display movies if found
                return render_template("movie_director_dashboard.html", movies=movies)
            else:
                # Handle case when no movies are found
                #print("error")
                error_message = "No movies found for the specified director."
                return render_template("movie_director_form.html", error_message=error_message)

        # Direct access to the movie dashboard without form submission
        print("Direct Access to Movie Director Dashboard")
        return render_template("movie_director_dashboard.html", movies=None)

    except Exception as e:
        # Log the error for debugging purposes
        print(f"Error: {e}")

        # Render the form template with an error message
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
            # Get form data
            actor_name = request.form.get("actor_name")

            print("Received Form Data:", actor_name)  # Check form data

            # Call function to get movies based on user criteria
            movies = search_movies_by_actor(actor_name)

            print("Movies Retrieved:", movies)  # Check movies retrieved

            if movies:
                # Display movies if found
                return render_template("movie_actor_dashboard.html", movies=movies)
            else:
                # Handle case when no movies are found
                error_message = "No movies found for the specified actor or actress."
                return render_template("movie_actor_form.html", error_message=error_message)

        # Direct access to the movie dashboard without form submission
        print("Direct Access to Movie Actor Dashboard")
        return render_template("movie_actor_dashboard.html", movies=None)

    except Exception as e:
        # Log the error for debugging purposes
        print(f"Error: {e}")

        # Render the form template with an error message
        error_message = "An error occurred. Please check your input and try again."
        return render_template("movie_actor_form.html", error_message=error_message)

@movie_routes.route("/api/movies.json")
def movies_api():
    print("MOVIES DATA (API)...")

    # For data supplied via GET request, URL params are in request.args:
    url_params = dict(request.args)
    print("URL PARAMS:", url_params)
    
    # Get parameters for movie search
    genre_id = url_params.get("genre_id")
    start_year = url_params.get("start_year")
    end_year = url_params.get("end_year")
    lang = url_params.get("lang")

    try:
        # Call function to get movies based on user criteria
        movies = search_movies_by_genre(genre_id, start_year, end_year, lang)

        if movies:
            # Convert movie data to dictionary records
            data = [movie.to_dict() for movie in movies]
            return {"genre_id": genre_id, "data": data}
        else:
            return {"message": "No movies found for the specified criteria."}, 404

    except Exception as err:
        print('OOPS', err)
        return {"message": "Movie data retrieval error. Please try again."}, 500
