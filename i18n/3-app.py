#!/usr/bin/env python3
"Basic Flask app"
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """ config class """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/')
def root():
    """ render 3-index.html """
    return render_template("3-index.html")


@babel.localeselector
def get_locale():
    """
    to Determine the best match with our supported languages.
    """
    lang = request.args.get('lang')
    if lang in app.config['LANGUAGES']:
        return lang
    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel = Babel(app, locale_selector=get_locale)

if __name__ == "__main__":
    app.run()
