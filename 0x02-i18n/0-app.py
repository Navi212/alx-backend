#!/usr/bin/env python3
""" app module  """
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    """ A function that returns an index page when queried at its / """
    return render_template("0-index.html", title="Welcome to Holberton")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
