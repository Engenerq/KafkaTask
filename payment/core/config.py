from pydantic import PostgresDsn
from pydantic_settings import BaseSettings
from functools import lru_cache


class SettingsPostgres(BaseSettings):
    dsn: PostgresDsn


class SettingsKafka(BaseSettings):
    host: str
    port: int


class SettingsTopicKafka(BaseSettings):
    order: str = "new_orders"
    payed: str = "payed_orders"


class Settings(BaseSettings):
    # Настройки проекта FasAPI
    debug: bool = False
    docs_url: str = "/docs"
    openapi_prefix: str = ""
    openapi_url: str = "/openapi.json"
    redoc_url: str = "/redoc"
    title: str = "Payment"
    version: str = "1.0.0"
    kafka: SettingsKafka
    kafka_topic: SettingsTopicKafka = SettingsTopicKafka()
    postgres: SettingsPostgres

    @property
    def fastapi_settings(self) -> dict[str, ...]:
        return {
            "debug": self.debug,
            "docs_url": self.docs_url,
            "openapi_prefix": self.openapi_prefix,
            "openapi_url": self.openapi_url,
            "redoc_url": self.redoc_url,
            "title": self.title,
            "version": self.version,
        }

    class Config:
        env_nested_delimiter = "__"
        nested_model_default_partial_update = True


@lru_cache()
def get_settings() -> Settings:
    return Settings()
