"""Settings."""

from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    """App settings."""
    ...

    model_config = SettingsConfigDict(env_file=".env")
