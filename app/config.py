from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    ELASTICSEARCH_HOST: str = "localhost"
    ELASTICSEARCH_PORT: int = 9200
    MOVIES_API_BASE_URL: str = "https://jsonmock.hackerrank.com/api/moviesdata/search"

    class Config:
        env_file = ".env"

settings = Settings()