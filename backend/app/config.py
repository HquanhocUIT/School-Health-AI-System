"""Environment based application configuration."""

import os

from dotenv import load_dotenv


load_dotenv()


def _parse_origins(value: str | None) -> list[str]:
    if not value:
        return ["http://localhost:3000", "http://localhost:5173"]
    return [origin.strip() for origin in value.split(",") if origin.strip()]


class Settings:
    """Settings read from the process environment (and a local .env file)."""

    def __init__(self) -> None:
        self.database_url: str | None = os.getenv("DATABASE_URL") or None
        self.cors_origins: list[str] = _parse_origins(os.getenv("CORS_ORIGINS"))


settings = Settings()
