# mypy: disable-error-code=call-arg
from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Arlette"
    debug: bool = True

    postgres_dsn: str = (
        "postgresql+psycopg://arlette:arlette@localhost:5432/arlette"
    )
    redis_url: str

    openai_api_key: str = ""

    llm_provider: str = "mistral"
    ollama_base_url: str = "http://localhost:11434"
    ollama_model: str = "mistral"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()