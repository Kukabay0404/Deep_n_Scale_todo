from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8', extra='allow')

    DATABASE_URL : str
    JWT_SECRET_KEY : str
    JWT_ALG : str
    ACCESS_TOKEN_EXPIRE_SECONDS : int
    START_DB : int
    SECRET_TOKEN : str
    VERIFICATION_TOKEN_SECRET : str

@lru_cache
def get_settings() -> Settings:
    return Settings()