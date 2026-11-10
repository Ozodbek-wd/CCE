import logging
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    environment: str = "development"
    log_level: str = "INFO"

    model_config = SettingsConfigDict(
        env_prefix="CCE_",
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    @property
    def logger(self) -> logging.Logger:
        logging.basicConfig(level=getattr(logging, self.log_level.upper(), logging.INFO))
        return logging.getLogger("cce")


settings = Settings()
