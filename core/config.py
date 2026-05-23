from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Arlette"
    debug: bool = False

    postgres_dsn: str
    redis_url: str

    openai_api_key: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )


@lru_cache
def get_settings() -> Settings:
    settings = Settings()  # type: ignore[call-arg]
    return settings