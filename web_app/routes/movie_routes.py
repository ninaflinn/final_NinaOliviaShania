from flask import Blueprint, request, render_template, redirect, flash, jsonify
import requests
from app.alpha import MOVIE_API_KEY  # Assuming MOVIE_API_KEY is imported from the correct location
from app.email_service import send_email
from app.movies_by_genre import get_genre_list

movies_routes = Blueprint("movies_routes", __name__)

@movies_routes.route("/movies/genres")
def movies_genres():
    print("MOVIES GENRES...")

    try:
        genres = get_genre_list()
        if genres:
            return render_template("movies_genres.html", genres=genres)
        else:
            flash("Failed to retrieve the list of genres.", "danger")
            return redirect("/movies/form")  # Redirect to the movies form or another suitable route

    except Exception as err:
        print('OOPS', err)
        flash("Error fetching movie genres. Please try again!", "danger")
        return redirect("/movies/form")  # Redirect to the movies form or another suitable route

@movies_routes.route("/movies/search", methods=["GET", "POST"])
def movies_search():
    print("MOVIES SEARCH...")

    if request.method == "POST":
        request_data = dict(request.form)
    else:
        request_data = dict(request.args)

    genre_id = request_data.get("genre_id") or '28'  # Default genre ID for Action

    start_year = request_data.get("start_year")
    end_year = request_data.get("end_year")
    lang = request_data.get("lang")

    try:
        # Use genre_id to search for movies based on the selected genre
        # Perform movie search based on other parameters (start_year, end_year, lang) similarly

        # Example usage of genre_id:
        # movies = search_movies_by_genre(genre_id, start_year, end_year, lang)

        flash("Fetched Movies Data!", "success")
        return render_template("movies_results.html", movies=movies)  # Pass movies data to template

    except Exception as err:
        print('OOPS', err)
        flash("Error fetching movies. Please try again!", "danger")
        return redirect("/movies/form")  # Redirect to the movies form or another suitable route
