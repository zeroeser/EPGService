from pydantic import BaseSettings


class Settings(BaseSettings):
    API_PATH: str = "/epg"
    PROJECT_NAME: str = "EPG"


settings = Settings()
