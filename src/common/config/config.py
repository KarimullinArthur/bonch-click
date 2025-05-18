from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    database_url: str = Field("DATABASE_URL")
    admin_username: str = Field("ADMIN_USERNAME")
    admin_password: str = Field("ADMIN_PASSWORD")
    jwt_secret: str = Field("JWT_SECRET")
    jwt_algorithm: str = "HS256"
    debug: bool = bool(Field("DEBUG"))

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
