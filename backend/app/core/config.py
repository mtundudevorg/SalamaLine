from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DATABASE_URL: str
    APP_NAME: str
    DEBUG:bool
    DESCRIPTION:str
    VERSION:str
    SECRET_KEY:str
    EXPIRE_ACCESS_TOKEN:int
    ALGORITHM:str
    RESEND_API_KEY:str
    EMAIL_FROM:str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()