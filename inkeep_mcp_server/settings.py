from pydantic_settings import BaseSettings, SettingsConfigDict


class InkeepSettings(BaseSettings):
    INKEEP_API_BASE_URL: str
    INKEEP_API_KEY: str
    INKEEP_API_MODEL: str
    INKEEP_MCP_TOOL_NAME: str = "search-product-content"
    INKEEP_MCP_TOOL_DESCRIPTION: str = (
        "Retrieve product content (docs, release notes, help center articles, etc.) about your product. Use when a task requires documentation or knowledge about the product that the user is a member of. Typical users include technical writers, content marketers,support agents, and developers who may be doing a task that requires knowledge about their own product, like writing a new blog post, modifying existing docs, creating examples, etc. The query can be framed as a conversational question about the product."
    )

    model_config = SettingsConfigDict()


inkeep_settings = InkeepSettings()  # type: ignore
