import os
from pydantic_settings import BaseSettings, SettingsConfigDict

DB_URL_GOLIVE = os.getenv("DB_URL_GOLIVE")
DB_NAME_GOLIVE = os.getenv("DB_NAME_GOLIVE")
DB_URL_CHATGPT = os.getenv("DB_URL_CHATGPT")
DB_NAME_CHATGPT = os.getenv("DB_NAME_CHATGPT")
OPEN_AI_KEY = os.getenv("OPEN_AI_KEY")
OPEN_AI_MODEL = os.getenv("OPEN_AI_MODEL")

class Settings(BaseSettings):
    DB_URL_GOLIVE: str = f"{DB_URL_GOLIVE}"
    DB_NAME_GOLIVE: str = f"{DB_NAME_GOLIVE}"
    DB_URL_CHATGPT: str = f"{DB_URL_CHATGPT}"
    DB_NAME_CHATGPT: str = f"{DB_NAME_CHATGPT}"
    OPEN_AI_KEY: str = f"{OPEN_AI_KEY}"
    OPEN_AI_MODEL: str = f"{OPEN_AI_MODEL}"
    TOKEN_LIMIT: int = 4096
    MAX_RESPONSE_TOKENS: int = 250
    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
