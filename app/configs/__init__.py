import os
from pydantic_settings import BaseSettings

DB_URL_GOLIVE = os.getenv("DB_URL_GOLIVE")
DB_NAME_GOLIVE = os.getenv("DB_NAME_GOLIVE")
DB_URL_CHATGPT = os.getenv("DB_URL_CHATGPT")
DB_NAME_CHATGPT = os.getenv("DB_NAME_CHATGPT")


class DatabaseSettings(BaseSettings):
    DB_URL_GOLIVE: str = f"{DB_URL_GOLIVE}"
    DB_NAME_GOLIVE: str = f"{DB_NAME_GOLIVE}"
    DB_URL_CHATGPT: str = f"{DB_URL_CHATGPT}"
    DB_NAME_CHATGPT: str = f"{DB_NAME_CHATGPT}"


class ChatGptSettings(BaseSettings):
    pass


class Settings(DatabaseSettings):
    pass


settings = Settings()
