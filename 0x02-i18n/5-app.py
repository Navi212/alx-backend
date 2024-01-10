#!/usr/bin/env python3
""" The `5-app` module mocks a database user table. """
from flask import Flask, render_template, request, g
from flask_babel import Babel

app = Flask(__name__)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """ A Language configuration class """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


def get_locale():
    """
    Returns the locale based on the passed locale param
    Else if no valid locale param passed, return the defualt locale
    """
    locale = request.args.get("locale")
    if locale not in Config.LANGUAGES:
        return request.accept_languages.best_match(app.config["LANGUAGES"])
    return locale


babel = Babel(app, locale_selector=get_locale)


@app.route("/")
def index():
    """ Serves requests when queried at / """
    return render_template("4-index.html")


def get_user():
    """ Returns a users dictionary if id if found of none if not """
    ids = request.args.get("login_as")
    if ids:
        return users.get(int(ids))
    return None


@app.before_request
def before_request():
    """ A function that gets executed before any other """
    g.user = get_user()
    return render_template("5-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
