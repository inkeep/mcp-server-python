# mcp-server-python
Inkeep MCP Server powered by your docs and product content.

### Dependencies

- An account on [Inkeep](https://inkeep.com) to manage and provide the RAG
- [`uv`](https://github.com/astral-sh/uv) Python project manager

### Local Setup

```
git clone https://github.com/inkeep/mcp-server-python.git
cd mcp-server-python
uv venv
uv pip install -r pyproject.toml
```

Note the full path of the project, referred to as `<YOUR_INKEEP_MCP_SERVER_ABSOLUTE_PATH>` in a later step.

## Get an API key

1. Log in to the [Inkeep Dashboard](https://portal.inkeep.com)
2. Navigate to the **Projects** section and select your project
3. Open the **Integrations** tab
4. Click **Create Integration** and choose **API** from the options
5. Enter a Name for your new API integration.
6. Click on **Create**
7. A generated **API key** will appear that you can use to authenticate API requests.

We'll refer to this API key as the `<YOUR_INKEEP_API_KEY>` in later steps.

### Add to your MCP client

Follow the steps in [this](https://modelcontextprotocol.io/quickstart/user) guide to setup Claude Dekstop.

In your `claude_desktop_config.json` file, add the following entry to `mcpServers`.

```json claude_desktop_config.json
{
    "mcpServers": {
        "inkeep-mcp-server": {
            "command": "uv",
            "args": [
                "--directory",
                "<YOUR_INKEEP_MCP_SERVER_ABSOLUTE_PATH>",
                "run",
                "-m",
                "inkeep_mcp_server"
            ],
            "env": {
                "INKEEP_API_BASE_URL": "https://api.inkeep.com/v1",
                "INKEEP_API_KEY": "<YOUR_INKEEP_API_KEY>",
                "INKEEP_API_MODEL": "inkeep-rag",
                "INKEEP_MCP_TOOL_NAME": "search-product-content",
                "INKEEP_MCP_TOOL_DESCRIPTION": "Retrieves product documentation about Inkeep. The query should be framed as a conversational question about Inkeep."
            }
        },
    }
}
```

You may need to put the full path to the `uv` executable in the command field. You can get this by running `which uv` on MacOS/Linux or `where uv` on Windows.
