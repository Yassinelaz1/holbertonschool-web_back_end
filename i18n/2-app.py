#!/usr/bin/env python3
"Basic Flask app"
from flask import Flask, render_template,request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)

class Config:
    "Basic Babel setup"
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

@app.route('/')
def root():
    """ render 2-index.html """
    return render_template("2-index.html")

@babel.localeselector
def get_locale():
    """  to determine the best match with our supported languages. """
    lang = request.args.get('lang')
    if lang in app.config['LANGUAGES']:
        return lang
    return request.accept_languages.best_match(app.config['LANGUAGES'])

if __name__ == "__main__":
    app.run()