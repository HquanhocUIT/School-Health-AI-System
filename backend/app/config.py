"""Environment based application configuration."""

import os

from dotenv import load_dotenv
from sqlalchemy import URL


load_dotenv()


def _parse_origins(value: str | None) -> list[str]:
    if not value:
        return ["http://localhost:3000", "http://localhost:5173", "http://127.0.0.1:5173"]
    return [origin.strip() for origin in value.split(",") if origin.strip()]


class Settings:
    """Settings read from the process environment (and a local .env file)."""

    def __init__(self) -> None:
        self.database_url: str | URL | None = os.getenv("DATABASE_URL") or None
        postgres_host = os.getenv("POSTGRES_HOST")
        if self.database_url is None and postgres_host:
            self.database_url = URL.create(
                "postgresql+psycopg",
                host=postgres_host,
                database=os.environ["POSTGRES_DB"],
                username=os.environ["POSTGRES_USER"],
                password=os.environ["POSTGRES_PASSWORD"],
            )
        self.cors_origins: list[str] = _parse_origins(os.getenv("CORS_ORIGINS"))


settings = Settings()
