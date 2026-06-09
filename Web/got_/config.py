import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Valores padrão se não houver arquivo .env
    PROJECT_NAME: str = "API Cuidadores de Plantas"
    STRIPE_SECRET_KEY: str = os.getenv("STRIPE_SECRET_KEY", "sk_test_mock")
    
    class Config:
        env_file = ".env"

settings = Settings()