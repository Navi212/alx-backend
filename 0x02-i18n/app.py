#!/usr/bin/env python3
""" The `6-app` introduces a 'Use user locale' functionality """
import pytz.exceptions
from flask import Flask, render_template, request, g
from flask_babel import Babel
from pytz import timezone


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
    # Locale from URL parameters
    locale = request.args.get("locale")
    if locale in app.config["LANGUAGES"]:
        return locale
    # Locale from user settings
    if g.user:
        locale = g.user.get("locale")
        if locale in app.config["LANGUAGES"]:
            return locale
    # Locale from request header
    locale = request.headers.get("locale")
    if locale in app.config["LANGUAGES"]:
        return locale
    # Default locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])


def get_timezone():
    """ Returns timezone """
    user_timezone = request.args.get("timezone")
    if user_timezone:
        try:
            return timezone(user_timezone)
        except pytz.exceptions.UnknownTimeZoneError:
            pass
    if g.user:
        try:
            return timezone(g.user.get("timezone"))
        except pytz.exceptions.UnknownTimeZoneError:
            pass
    return app.config["BABEL_DEFAULT_TIMEZONE"]


babel = Babel(app, locale_selector=get_locale, timezone_selector=get_timezone)


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
    return render_template("7-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
