from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    openai_api_key: str
    openai_model: str = "gpt-5.4"
    app_env: str = "development"
    allowed_origins: str = "http://localhost:5500,http://127.0.0.1:5500"
    knowledge_dir: str = "../knowledge"
    max_chunks_per_query: int = 6
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    @property
    def cors_origins(self) -> list[str]:
        return [item.strip() for item in self.allowed_origins.split(",") if item.strip()]

settings = Settings()
