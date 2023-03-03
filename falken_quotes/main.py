# by Richi Rod AKA @richionline / falken20
# ./falken_quotes/main.py

from flask import Flask, render_template
from dotenv import load_dotenv, find_dotenv

from .logger import Log
from .config import get_settings
from .quotes import get_api_quote
from .chatgpt import translate

# Set environment vars
load_dotenv(find_dotenv())

app = Flask(__name__, template_folder="../templates",
            static_folder="../static")
app.config['TEMPLATE_AUTO_RELOAD'] = True

settings = get_settings()
Log.info(f"Settings: {settings}")


@app.route("/")
@app.route("/home")
def home():
    Log.info("Access to home page")

    dict_quote = get_api_quote(url=settings.api_url)
    quote_translated = translate(lang="spanish", text_to_translate=dict_quote[0]['q'])

    Log.debug(f"{dict_quote[0]['q']}")

    return render_template("index.html", 
                            quote=dict_quote[0]["q"], 
                            quote_translated=quote_translated,
                            author=dict_quote[0]["a"])


if __name__ == "__main__":
    app.run()
