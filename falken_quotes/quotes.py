# by Richi Rod AKA @richionline / falken20
# ./falken_quotes/quotes.py

import requests
import json
import sys

from .logger import Log

def get_api_quote(url: str) -> dict:
    """Proccess to get the quote from the API

    Args:
        url (str): URL for getting the quote
    """
    Log.info(f"Proccess to getting quote from API")
    Log.debug(f"API url: {url}")

    try:
        response = requests.get(url)
        dict_quote = json.loads(response.text)

        Log.debug(f"API data JSON: {dict_quote}")

        return dict_quote

    except Exception as err:
        Log.error("Error getting data from API", err, sys)
        return {}        