# by Richi Rod AKA @richionline / falken20
# url_shortener/config.py

# Library that uses type annotation to validate data and manage settings.
from pydantic import BaseSettings
# Library to cache the data
from functools import lru_cache


class Settings(BaseSettings):
    # pydantic will automatically assume those default values if it doesn’t
    # find the corresponding environment variables.
    env_name: str = "Local"
    base_url: str = "http://localhost:5000"
    # db_url: str = "sqlite:///./shortener.db"
    ENV_PRO: str = "N"
    LEVEL_LOG: list = []
    API_URL_QUOTES: str = "https://zenquotes.io/api/random"
    OPENAI_API_KEY: str = "my-api-key"
    API_URL_TRANSLATE: str = "https://nlp-translation.p.rapidapi.com/v1/translate"
    API_KEY: str = "my-api-key"

    class Config:
        # When you add the Config class with the path to your env_file to your
        # settings, pydantic loads your environment variables from the .env file.
        env_file = ".env"


@lru_cache
def get_settings() -> Settings:
    settings = Settings()
    print(f"Loading settings for: {settings.env_name}")
    return settings
