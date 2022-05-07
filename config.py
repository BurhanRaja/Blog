from pydantic import BaseSettings

class Settings(BaseSettings):
    secret_key: str
    email_host: str
    email_host_user: str
    email_host_password: str

    class Config:
        env_file = ".env"

settings = Settings()