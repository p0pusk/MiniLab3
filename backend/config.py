import os
from pydantic import BaseSettings
from typing import List


class Settings(BaseSettings):
    VERSION: str = "0.1.0"

    CORS_ORIGINS: List[str] = ["*"]
    PORT: int = int(os.environ["PORT"])
    URL_PREFIX: str = "/minilab3"


settings = Settings()
