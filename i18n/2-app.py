#!/usr/bin/env python3
"Basic Flask app"
from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)


app.config['LANGUAGES'] = ['en', 'fr']
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'


def get_locale():
    """
    to Determine the best match with our supported languages.
    """
    lang = request.args.get('lang')
    if lang in app.config['LANGUAGES']:
        return lang
    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel = Babel(app, locale_selector=get_locale)


@app.route('/')
def index():
    """render 2-index.html"""
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(debug=True)
