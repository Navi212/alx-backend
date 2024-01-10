#!/usr/bin/env python3
""" The `4-app` module forces return of a particular locale """
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)


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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
