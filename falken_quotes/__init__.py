# by Richi Rod AKA @richionline / falken20
# ./falken_quotes/__init__.py

from flask import Flask, render_template

from .config import get_settings
from falken_quotes.logger import Log

__title__ = 'Falken Quotes'
__version__ = '1.0.1'
__author__ = 'Falken'
__url_github__ = 'https://github.com/falken20/'
__url_twitter__ = 'https://twitter.com/richionline'
__url_linkedin__ = 'https://www.linkedin.com/in/richionline/'
__license__ = 'MIT License'
__copyright__ = '© 2022 by Richi Rod AKA @richionline / falken20'
__features__ = [
]


SETUP_DATA = {
    'title': __title__,
    'version': __version__,
    'author': __author__,
    'url_github': __url_github__,
    'url_twitter': __url_twitter__,
    'url_linkedin': __url_linkedin__,
    'license': __license__,
    'copyrigth': __copyright__,
    'features': __features__,
}


app = Flask(__name__, template_folder="../templates",
            static_folder="../static")
app.config['TEMPLATE_AUTO_RELOAD'] = True

settings = get_settings()
Log.info(f"Settings: {settings}")