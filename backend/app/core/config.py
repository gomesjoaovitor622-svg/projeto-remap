from functools import lru_cache
from pydantic import Field, model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "REMAP API"
    app_env: str = "development"
    database_url: str = "postgresql+psycopg://remap_app:CHANGE_ME@localhost:5432/remap"
    jwt_secret_key: str = Field(default="development-only-change-this-secret-key-123456", min_length=32)
    jwt_algorithm: str = "HS256"
    access_token_minutes: int = Field(default=30, ge=5, le=1440)
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    @model_validator(mode="after")
    def reject_development_secret_in_production(self):
        if self.app_env.lower() == "production" and self.jwt_secret_key.startswith("development-only-"):
            raise ValueError("Defina JWT_SECRET_KEY forte antes de executar em produção.")
        return self

@lru_cache
def get_settings() -> Settings:
    return Settings()

settings = get_settings()
