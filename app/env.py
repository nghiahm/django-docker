from pydantic import BaseSettings
import os

class Settings(BaseSettings):
    
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: str

    DJANGO_SUPERUSER_USERNAME: str
    DJANGO_SUPERUSER_EMAIL: str
    DJANGO_SUPERUSER_PASSWORD: str
    
    class Config:
        case_sensitive = True

env = Settings(_env_file='.env')
