# by Richi Rod AKA @richionline / falken20
# ./falken_quotes/api_translate.py

import requests

from falken_quotes.logger import Log
from . import settings

url = settings.API_URL_TRANSLATE
api_key = settings.API_KEY


def translate(source: str = "en", to: str = "es", text_to_translate: str = "Hello") -> str:
    """Translate a text FROM languaje TO another languaje

    Args:
        source (str, optional): Source languaje. Defaults to "en".
        to (str, optional): Destination languaje. Defaults to "es".
        text_to_translate (str, optional): Text to translate. Defaults to "Hello".

    Returns:
        str: Text translated
    """

    Log.info("Starting to translate the text...")
    Log.debug(f"Translate this into {to}: {text_to_translate}")

    query = {
        "text": text_to_translate,
        "to": to,
        "from": source,
    }

    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "nlp-translation.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=query)

    translated_text = response.json()
    # If there is an error in the API only return json with "message" key
    if translated_text['message']:
        Log.warning(f"Problems with translation: {translated_text['message']}")
        translated_text = ""
    else:
        translated_text = translated_text['translated_text']
        Log.debug(f"Translated text: {translated_text}")

    # return response.choices[0].text.strip()
    return translated_text
