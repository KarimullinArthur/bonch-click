from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    database_url: str = Field("DATABASE_URL")
    debug: bool = Field("DEBUG")

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
