import openai
import os

from falken_quotes.logger import Log

openai.api_key = os.getenv("OPENAI_API_KEY")
model_engine = "text-davinci-003"


def translate(lang: str = "spanish", text_to_translate: str = "Hello") -> str:
    """ Translate the text in english to spanish

    Args:
        lang (str): Language
        text_to_translate (str): Text in english

    Returns:
        str: Text tranlate to lang (language)
    """
    Log.info("Starting to translate the text with OpenAI...")

    text_to_translate = f"Translate this into {lang}: {text_to_translate}"

    response = openai.Completion.create(
        model=model_engine,
        prompt=text_to_translate,
        temperature=0.3,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    Log.debug(f"Translated text: {response.choices[0].text.strip()}")
    return response.choices[0].text.strip()
