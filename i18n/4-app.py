#!/usr/bin/env python3
"Basic Flask app"
from flask import Flask, render_template, request
from flask_babel import Babel, gettext


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
    """ render 4-index.html """
    return render_template("4-index.html")


@babel.localeselector
def get_locale():
    """
    to Determine the best match with our supported languages.
    """
    local_Lang = request.args.get('locale')
    supportLang = app.config['LANGUAGES']
    if local_Lang in supportLang:
        return local_Lang
    else:
        return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run()
