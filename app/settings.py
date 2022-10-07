from pydantic import BaseSettings


class Settings(BaseSettings):
    API_PATH: str = ""
    PROJECT_NAME: str = "EPG"


settings = Settings()
