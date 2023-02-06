from typing import Any, Optional

from dotenv import find_dotenv
from pydantic import BaseSettings, PostgresDsn, validator


class Settings(BaseSettings):
    class Config:
        env_file = find_dotenv(usecwd=True)
        env_file_encoding = "utf-8"
        case_sensitive = True

    SERVER_HOST: str
    SERVER_PORT: int
    APP_DOMAIN: str
    APP_PREFIX: str = "/auth"
    SHARED_ACCESS_TOKEN: str

    # Postgres DB
    DATABASE_HOST: str
    DATABASE_USER: str
    DATABASE_PASSWORD: str
    DATABASE_NAME: str
    DATABASE_URI: Optional[str] = None

    # JWT
    ALGORITHM: str
    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    @validator("DATABASE_URI")
    def construct_database_connection_uri(cls, v: Optional[str], values: dict[str, Any]) -> str | PostgresDsn:
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="postgresql",
            host=values.get("DATABASE_HOST"),
            user=values.get("DATABASE_USER"),
            password=values.get("DATABASE_PASSWORD"),
            path=f"/{values.get('DATABASE_NAME') or ''}",
        )
