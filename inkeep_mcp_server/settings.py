from pydantic_settings import BaseSettings, SettingsConfigDict


class InkeepSettings(BaseSettings):
    INKEEP_API_BASE_URL: str
    INKEEP_API_KEY: str
    INKEEP_API_MODEL: str

    model_config = SettingsConfigDict()


inkeep_settings = InkeepSettings()  # type: ignore
