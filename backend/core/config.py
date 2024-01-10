import os
from dotenv import load_dotenv

from pathlib import Path
env_path = Path(__file__).resolve().parent.parent / '.env'
# print(env_path.resolve())
load_dotenv(dotenv_path=env_path)


class Settings:
    PROJECT_NAME: str = "ThisIsBase"
    PROJECT_VERSION : str = "0.1.0"

    POSTGRES_USER: str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER", "localhost")
    POSTGRES_PORT: str = os.getenv("POSTGRES_PORT", 5432)  # default postgres port is 5432
    POSTGRES_DB: str = os.getenv("POSTGRES_DB", "blogdb")
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"


settings = Settings()
# print(settings.POSTGRES_USER, settings.POSTGRES_PASSWORD)