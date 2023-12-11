
# this is the "web_app/routes/stocks_routes.py" file ...

from flask import Blueprint, request, render_template, redirect, flash

from app.stocks import fetch_stocks_data, format_usd

movie_routes = Blueprint("movie_routes", __name__)

@movie_routes.route("/movie/form")
def movies_form():
    print("MOVIE FORM...")
    return render_template("movie_form.html")

@movie_routes.route("/movie/dashboard", methods=["GET", "POST"])
def movies_dashboard():
    print("STOCKS DASHBOARD...")

    if request.method == "POST":
        # for data sent via POST request, form inputs are in request.form:
        request_data = dict(request.form)
        print("FORM DATA:", request_data)
    else:
        # for data sent via GET request, url params are in request.args
        request_data = dict(request.args)
        print("URL PARAMS:", request_data)

    symbol = request_data.get("symbol") or "NFLX"

    try:
        df = fetch_stocks_data(symbol=symbol)
        latest_close_usd = format_usd(df.iloc[0]["adjusted_close"])
        latest_date = df.iloc[0]["timestamp"]
        data = df.to_dict("records")

        flash("Fetched Real-time Market Data!", "success")
        return render_template("movie_dashboard.html",
            symbol=symbol,
            latest_close_usd=latest_close_usd,
            latest_date=latest_date,
            data=data
        )
    except Exception as err:
        print('OOPS', err)

        flash("Market Data Error. Please check your symbol and try again!", "danger")
        return redirect("/movie/form")

#
# API ROUTES
#

@movie_routes.route("/api/stocks.json")
def movie_api():
    print("STOCKS DATA (API)...")

    # for data supplied via GET request, url params are in request.args:
    url_params = dict(request.args)
    print("URL PARAMS:", url_params)
    symbol = url_params.get("symbol") or "NFLX"

    try:
        df = fetch_stocks_data(symbol=symbol)
        data = df.to_dict("records")
        return {"symbol": symbol, "data": data }
    except Exception as err:
        print('OOPS', err)
        return {"message":"Market Data Error. Please try again."}, 404